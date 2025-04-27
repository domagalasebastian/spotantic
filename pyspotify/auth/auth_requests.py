import asyncio
import webbrowser
from typing import Any
from typing import Dict
from typing import Optional
from urllib.parse import urlencode
from urllib.parse import urlparse

from aiohttp import BasicAuth
from aiohttp import ClientSession
from aiohttp import web

from .access_token_info import AccessTokenInfo

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
ACCESS_TOKEN_REQUEST_CONTENT_TYPE = "application/x-www-form-urlencoded"


async def get_access_token(*, data: Dict[str, Any], auth: Optional[BasicAuth] = None) -> AccessTokenInfo:
    headers = {
        "Content-Type": ACCESS_TOKEN_REQUEST_CONTENT_TYPE,
    }

    async with ClientSession() as session:
        async with session.post(TOKEN_URL, headers=headers, auth=auth, data=data) as response:
            payload = await response.json()
            if response.status != 200:
                raise Exception(f"Failed to get access token! Payload: {payload}")

        return AccessTokenInfo(**payload)


async def get_code(*, redirect_uri: str, params: Dict[str, Any]) -> str:
    state = params.get("state")
    code = None

    async def callback(request) -> web.Response:
        nonlocal code
        r_state = request.query.get("state")
        if state is not None and r_state != state:
            raise Exception("Wrong state received in reponse!")

        code = request.query.get("code")
        return web.Response(text="OK")

    target_url = f"{AUTH_URL}?{urlencode(params)}"
    server_address_parsed = urlparse(redirect_uri)

    app = web.Application()
    app.router.add_get("/callback", callback)
    runner = web.AppRunner(app)
    await runner.setup()
    try:
        site = web.TCPSite(runner, host=server_address_parsed.hostname, port=server_address_parsed.port)
        await site.start()
    except Exception:
        raise
    else:
        webbrowser.open(target_url)

        while code is None:
            await asyncio.sleep(1)
    finally:
        await runner.cleanup()

    return code
