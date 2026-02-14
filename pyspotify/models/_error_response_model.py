from __future__ import annotations

from http import HTTPStatus

from pydantic import BaseModel


class ErrorResponseModel(BaseModel):
    """Model representing error information from unsuccessful Spotify API responses.

    This model parses the error payload returned by the Spotify API when a request fails.
    """

    status: HTTPStatus
    """The HTTP status code that is also returned in the response header."""

    message: str
    """A short description of the cause of the error."""
