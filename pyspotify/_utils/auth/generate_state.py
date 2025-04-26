import base64
import hashlib
import secrets
import string


def generate_random_string(length) -> str:
    allowed_chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(allowed_chars) for _ in range(length))


def generate_oauth2_state(random_string: str) -> str:
    hashed = hashlib.sha256(random_string.encode("ascii")).digest()
    return base64.urlsafe_b64encode(hashed).rstrip(b"=").decode("ascii")
