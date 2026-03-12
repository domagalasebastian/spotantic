from pydantic import BaseModel

from spotantic.types import SpotifyMarketID


class GetAvailableMarketsResponse(BaseModel):
    """Response model for Get Available Markets endpoint."""

    markets: list[SpotifyMarketID]
    """List of available markets."""
