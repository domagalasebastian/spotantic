from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import RequestModel


class GetSingleBrowseCategoryRequestParams(BaseModel):
    """Params model for Get Single Browse Category request."""

    locale: Optional[SpotifyLocaleID] = None
    """
    The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code,
    joined by an underscore.
    """

    category_id: str
    """The Spotify ID for the browse category."""


class GetSingleBrowseCategoryRequest(RequestModel[GetSingleBrowseCategoryRequestParams, None]):
    """Request model for Get Single Browse Category endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        category_id: str,
        locale: Optional[SpotifyLocaleID] = None,
    ) -> GetSingleBrowseCategoryRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            category_id: The Spotify ID for the browse category.
            locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code,
             joined by an underscore.

        Returns:
            Validated Request object.
        """
        params = GetSingleBrowseCategoryRequestParams(
            locale=locale,
            category_id=category_id,
        )

        endpoint = f"browse/categories/{category_id}"

        return cls(endpoint=endpoint, params=params)
