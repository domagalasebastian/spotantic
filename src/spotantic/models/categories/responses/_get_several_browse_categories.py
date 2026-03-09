from pydantic import BaseModel

from spotantic.models.spotify import CategoryModel
from spotantic.models.spotify import PagedResultModel


class GetSeveralBrowseCategoriesResponse(BaseModel):
    """Response model for Get Several Browse Categories endpoint."""

    categories: PagedResultModel[CategoryModel]
    """List of categories."""
