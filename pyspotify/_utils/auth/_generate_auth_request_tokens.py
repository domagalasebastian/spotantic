import base64
import hashlib
import secrets


def generate_url_safe_token(length: int) -> str:
    """Generate URL-safe token of given length.

    Args:
        length: Expected length of a token.

    Returns:
        URL-safe token of specified length.
    """
    return secrets.token_urlsafe(length)


def generate_pkce_code_verifier(entropy_length: int) -> str:
    """Generate a Code Verifier for Authorization Code with PKCE Flow.

    Args:
        entropy_length: Length of an entropy.

    Returns:
        PKCE Code Verifier.
    """
    entropy = secrets.token_bytes(entropy_length)
    return base64.urlsafe_b64encode(entropy).rstrip(b"=").decode("ascii")


def get_pkce_code_challenge(pkce_code_verifier: str) -> str:
    """Get PKCE Code Challenge for the specified PKCE Code Verifier.

    Args:
        pkce_code_verifier: PKCE Code Verifier.

    Returns:
        PKCE Code Challenge generated using `S256` method.
    """
    digest = hashlib.sha256(pkce_code_verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
