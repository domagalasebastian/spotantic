import asyncio
import webbrowser
from typing import Optional
from urllib.parse import urlencode
from urllib.parse import urlparse

from aiohttp import BasicAuth
from aiohttp import ClientSession
from aiohttp import web

from pyspotify._utils.auth.generate_state import generate_oauth2_state
from pyspotify._utils.auth.generate_state import generate_random_string

from .access_token_info import AccessTokenInfo
from .auth_manager_base import AuthManagerBase


class AuthCodeFlowManager(AuthManagerBase):
    __AUTH_URL = "https://accounts.spotify.com/authorize"
    __TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope: Optional[str] = None,
        env_file_path: Optional[str] = None,
    ) -> None:
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            env_file_path=env_file_path,
        )

        assert self.client_id is not None, "Client ID must be set"
        assert self.client_secret is not None, "Client Secret must be set"
        assert self.redirect_uri is not None, "Redirect URI must be set"
        assert self.scope is not None, "Scope must be set"

        self.__auth_header = BasicAuth(
            self.client_id,
            self.client_secret,
        )

    def __build_auth_url(self, state: str) -> str:
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": self.scope,
            "state": state,
        }

        return f"{self.__AUTH_URL}?{urlencode(params)}"

    async def __get_access_token(self, code: str) -> AccessTokenInfo:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": str(self.redirect_uri),
        }

        async with ClientSession() as session:
            async with session.post(self.__TOKEN_URL, auth=self.__auth_header, headers=headers, data=data) as response:
                payload = await response.json()
                if response.status != 200:
                    raise Exception(f"Failed to get access token! Payload: {payload}")

            return AccessTokenInfo(**payload)

    async def __get_code(self) -> str:
        state = generate_oauth2_state(generate_random_string(64))
        code = None

        async def callback(request) -> web.Response:
            nonlocal code
            r_state = request.query.get("state")
            if r_state != state:
                raise Exception("Wrong state received in reponse!")

            code = request.query.get("code")
            return web.Response(text="OK")

        target_url = self.__build_auth_url(state)
        server_address_parsed = urlparse(str(self.redirect_uri))
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

    async def authorize(self) -> AccessTokenInfo:
        code = await self.__get_code()
        token_info = await self.__get_access_token(code=code)

        if self._store_access_token:
            token_info.store_token(file_path=self._access_token_file_path)

        return token_info
