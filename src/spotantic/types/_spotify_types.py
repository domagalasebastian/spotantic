from __future__ import annotations

from enum import StrEnum


class SpotifyItemType(StrEnum):
    """Spotify object types."""

    ALBUM = "album"
    """Album."""

    ARTIST = "artist"
    """Artist."""

    EPISODE = "episode"
    """Episode."""

    PLAYLIST = "playlist"
    """Playlist."""

    SHOW = "show"
    """Show."""

    TRACK = "track"
    """Track."""

    USER = "user"
    """User."""


class AlbumTypes(StrEnum):
    """The type of the album."""

    ALBUM = "album"
    """Album."""

    SINGLE = "single"
    """Single."""

    APPEARS_ON = "appears_on"
    """Appears on."""

    COMPILATION = "compilation"
    """Compilation."""

    # NOTE: Spotify docs do not mention this type, but it is returned for some albums
    EP = "ep"
    """EP."""


class RepeatMode(StrEnum):
    """Possible repeat states."""

    TRACK = "track"
    """Repeat a track."""

    CONTEXT = "context"
    """Repeat a context."""

    OFF = "off"
    """Repeat off."""


class AuthScope(StrEnum):
    """Scopes provide Spotify users using third-party apps the confidence that only the information
    they choose to share will be shared, and nothing more."""

    PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"
    """Manage your private playlists."""

    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"
    """Manage your public playlists."""

    PLAYLIST_READ_PRIVATE = "playlist-read-private"
    """Access your private playlists."""

    UGC_IMAGE_UPLOAD = "ugc-image-upload"
    """Upload images to Spotify on your behalf."""

    USER_FOLLOW_MODIFY = "user-follow-modify"
    """Manage who you are following."""

    USER_FOLLOW_READ = "user-follow-read"
    """Access your followers and who you are following."""

    USER_LIBRARY_MODIFY = "user-library-modify"
    """Manage your saved content."""

    USER_LIBRARY_READ = "user-library-read"
    """Access your saved content."""

    USER_MODIFY_PLAYBACK_STATE = "user-modify-playback-state"
    """Control playback on your Spotify clients and Spotify Connect devices."""

    USER_READ_CURRENTLY_PLAYING = "user-read-currently-playing"
    """Read your currently playing content."""

    USER_READ_EMAIL = "user-read-email"
    """Get your real email address."""

    USER_READ_PLAYBACK_POSITION = "user-read-playback-position"
    """Read your position in content you have played."""

    USER_READ_PLAYBACK_STATE = "user-read-playback-state"
    """Read your currently playing content and Spotify Connect devices information."""

    USER_READ_PRIVATE = "user-read-private"
    """Access your subscription details."""

    USER_READ_RECENTLY_PLAYED = "user-read-recently-played"
    """Access your recently played items."""

    USER_TOP_READ = "user-top-read"
    """Read your top artists and content."""
