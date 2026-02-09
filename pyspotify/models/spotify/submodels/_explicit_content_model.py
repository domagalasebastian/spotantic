from pydantic import BaseModel


class ExplicitContentModel(BaseModel):
    """Model representing user's explicit content settings."""

    filter_enabled: bool
    """When `True`, indicates that explicit content should not be played."""

    filter_locked: bool
    """When `True`, indicates that the explicit content setting is locked and can't be changed by the user."""
