from pathlib import Path
from typing import Protocol

from ._access_token_info import AccessTokenInfo


class TokenStore(Protocol):
    """Protocol for a token store."""

    def save_token(self, token: AccessTokenInfo) -> None:
        """Save the token to the store.

        Args:
            token: The token to save.
        """
        ...

    def load_token(self) -> AccessTokenInfo | None:
        """Load the token from the store.

        Returns:
            The loaded token.
        """
        ...


class FileTokenStore:
    """A simple file-based token store."""

    def __init__(self, file_path: str | Path):
        """Initialize the FileTokenStore.

        Args:
            file_path: The path to the file where the token will be stored.
        """
        self.__file_path = file_path

    def save_token(self, token: AccessTokenInfo) -> None:
        """Save the token to a file.

        Args:
            token: The token to save.
        """
        with open(self.__file_path, "w") as fd:
            fd.write(token.model_dump_json())

    def load_token(self) -> AccessTokenInfo | None:
        """Load the token from a file.

        Returns:
            The loaded token.
        """
        path = Path(self.__file_path)
        if not path.exists():
            return None

        with open(self.__file_path, "r") as fd:
            json_data = fd.read()

        return AccessTokenInfo.model_validate_json(json_data=json_data)
