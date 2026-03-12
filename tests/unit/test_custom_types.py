import pytest
from pydantic import TypeAdapter
from pydantic import ValidationError

from spotantic.types import SpotifyAlbumURI
from spotantic.types import SpotifyArtistURI
from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyLocaleID
from spotantic.types import SpotifyMarketID
from spotantic.types import SpotifyPlaylistURI
from spotantic.types import SpotifyShowURI
from spotantic.types import SpotifyTrackURI
from spotantic.types import SpotifyUserURI


class TestSpotifyMarketID:
    """Tests for SpotifyMarketID type."""

    def test_valid_market_id(self):
        """Test valid market ID."""
        adapter = TypeAdapter(SpotifyMarketID)
        result = adapter.validate_python("US")
        assert result == "US"

    def test_market_id_convert_to_upper(self):
        """Test that market ID is converted to uppercase."""
        adapter = TypeAdapter(SpotifyMarketID)
        result = adapter.validate_python("us")
        assert result == "US"

    def test_market_id_strip_whitespace(self):
        """Test that market ID whitespace is stripped."""
        adapter = TypeAdapter(SpotifyMarketID)
        result = adapter.validate_python("  us  ")
        assert result == "US"

    def test_market_id_invalid_length(self):
        """Test that market ID with invalid length fails."""
        adapter = TypeAdapter(SpotifyMarketID)
        with pytest.raises(ValidationError):
            adapter.validate_python("USA")

    def test_market_id_invalid_pattern(self):
        """Test that market ID with invalid pattern fails."""
        adapter = TypeAdapter(SpotifyMarketID)
        with pytest.raises(ValidationError):
            adapter.validate_python("12")


class TestSpotifyLocaleID:
    """Tests for SpotifyLocaleID type."""

    def test_valid_locale_id(self):
        """Test valid locale ID."""
        adapter = TypeAdapter(SpotifyLocaleID)
        result = adapter.validate_python("en_US")
        assert result == "en_US"

    def test_locale_id_strip_whitespace(self):
        """Test that locale ID whitespace is stripped."""
        adapter = TypeAdapter(SpotifyLocaleID)
        result = adapter.validate_python("  en_US  ")
        assert result == "en_US"

    def test_locale_id_invalid_pattern(self):
        """Test that locale ID with invalid pattern fails."""
        adapter = TypeAdapter(SpotifyLocaleID)
        with pytest.raises(ValidationError):
            adapter.validate_python("en-US")

    def test_locale_id_invalid_length(self):
        """Test that locale ID with invalid length fails."""
        adapter = TypeAdapter(SpotifyLocaleID)
        with pytest.raises(ValidationError):
            adapter.validate_python("en_USA")


class TestSpotifyItemID:
    """Tests for SpotifyItemID type."""

    def test_valid_item_id(self):
        """Test valid item ID."""
        adapter = TypeAdapter(SpotifyItemID)
        result = adapter.validate_python("AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "AaBbCcDdEeFfGgHhIiJjKk"

    def test_item_id_strip_whitespace(self):
        """Test that item ID whitespace is stripped."""
        adapter = TypeAdapter(SpotifyItemID)
        result = adapter.validate_python("  AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "AaBbCcDdEeFfGgHhIiJjKk"

    def test_item_id_too_short(self):
        """Test that item ID with insufficient length fails."""
        adapter = TypeAdapter(SpotifyItemID)
        with pytest.raises(ValidationError):
            adapter.validate_python("AaBbCcDdEeFfGgHhIiJj")

    def test_item_id_too_long(self):
        """Test that item ID with excessive length fails."""
        adapter = TypeAdapter(SpotifyItemID)
        with pytest.raises(ValidationError):
            adapter.validate_python("AaBbCcDdEeFfGgHhIiJjKkL")

    def test_item_id_invalid_characters(self):
        """Test that item ID with invalid characters fails."""
        adapter = TypeAdapter(SpotifyItemID)
        with pytest.raises(ValidationError):
            adapter.validate_python("!@#$%^&*()_+-=[]{};;")


class TestSpotifyAlbumURI:
    """Tests for SpotifyAlbumURI type."""

    def test_valid_album_uri(self):
        """Test valid album URI."""
        adapter = TypeAdapter(SpotifyAlbumURI)
        result = adapter.validate_python("spotify:album:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:album:AaBbCcDdEeFfGgHhIiJjKk"

    def test_album_uri_strip_whitespace(self):
        """Test that album URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyAlbumURI)
        result = adapter.validate_python("  spotify:album:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:album:AaBbCcDdEeFfGgHhIiJjKk"

    def test_album_uri_invalid_type(self):
        """Test that album URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyAlbumURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:artist:AaBbCcDdEeFfGgHhIiJjKk")

    def test_album_uri_invalid_id_length(self):
        """Test that album URI with invalid ID length fails."""
        adapter = TypeAdapter(SpotifyAlbumURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:album:AaBbCcDdEeFfGgHhIiJj")


class TestSpotifyArtistURI:
    """Tests for SpotifyArtistURI type."""

    def test_valid_artist_uri(self):
        """Test valid artist URI."""
        adapter = TypeAdapter(SpotifyArtistURI)
        result = adapter.validate_python("spotify:artist:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:artist:AaBbCcDdEeFfGgHhIiJjKk"

    def test_artist_uri_strip_whitespace(self):
        """Test that artist URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyArtistURI)
        result = adapter.validate_python("  spotify:artist:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:artist:AaBbCcDdEeFfGgHhIiJjKk"

    def test_artist_uri_invalid_type(self):
        """Test that artist URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyArtistURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:album:AaBbCcDdEeFfGgHhIiJjKk")


class TestSpotifyEpisodeURI:
    """Tests for SpotifyEpisodeURI type."""

    def test_valid_episode_uri(self):
        """Test valid episode URI."""
        adapter = TypeAdapter(SpotifyEpisodeURI)
        result = adapter.validate_python("spotify:episode:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:episode:AaBbCcDdEeFfGgHhIiJjKk"

    def test_episode_uri_strip_whitespace(self):
        """Test that episode URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyEpisodeURI)
        result = adapter.validate_python("  spotify:episode:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:episode:AaBbCcDdEeFfGgHhIiJjKk"

    def test_episode_uri_invalid_type(self):
        """Test that episode URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyEpisodeURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:track:AaBbCcDdEeFfGgHhIiJjKk")


class TestSpotifyPlaylistURI:
    """Tests for SpotifyPlaylistURI type."""

    def test_valid_playlist_uri(self):
        """Test valid playlist URI."""
        adapter = TypeAdapter(SpotifyPlaylistURI)
        result = adapter.validate_python("spotify:playlist:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:playlist:AaBbCcDdEeFfGgHhIiJjKk"

    def test_playlist_uri_strip_whitespace(self):
        """Test that playlist URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyPlaylistURI)
        result = adapter.validate_python("  spotify:playlist:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:playlist:AaBbCcDdEeFfGgHhIiJjKk"

    def test_playlist_uri_invalid_type(self):
        """Test that playlist URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyPlaylistURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:album:AaBbCcDdEeFfGgHhIiJjKk")


class TestSpotifyShowURI:
    """Tests for SpotifyShowURI type."""

    def test_valid_show_uri(self):
        """Test valid show URI."""
        adapter = TypeAdapter(SpotifyShowURI)
        result = adapter.validate_python("spotify:show:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:show:AaBbCcDdEeFfGgHhIiJjKk"

    def test_show_uri_strip_whitespace(self):
        """Test that show URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyShowURI)
        result = adapter.validate_python("  spotify:show:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:show:AaBbCcDdEeFfGgHhIiJjKk"

    def test_show_uri_invalid_type(self):
        """Test that show URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyShowURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:track:AaBbCcDdEeFfGgHhIiJjKk")


class TestSpotifyTrackURI:
    """Tests for SpotifyTrackURI type."""

    def test_valid_track_uri(self):
        """Test valid track URI."""
        adapter = TypeAdapter(SpotifyTrackURI)
        result = adapter.validate_python("spotify:track:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:track:AaBbCcDdEeFfGgHhIiJjKk"

    def test_track_uri_strip_whitespace(self):
        """Test that track URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyTrackURI)
        result = adapter.validate_python("  spotify:track:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:track:AaBbCcDdEeFfGgHhIiJjKk"

    def test_track_uri_invalid_type(self):
        """Test that track URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyTrackURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:album:AaBbCcDdEeFfGgHhIiJjKk")


class TestSpotifyUserURI:
    """Tests for SpotifyUserURI type."""

    def test_valid_user_uri(self):
        """Test valid user URI."""
        adapter = TypeAdapter(SpotifyUserURI)
        result = adapter.validate_python("spotify:user:AaBbCcDdEeFfGgHhIiJjKk")
        assert result == "spotify:user:AaBbCcDdEeFfGgHhIiJjKk"

    def test_user_uri_strip_whitespace(self):
        """Test that user URI whitespace is stripped."""
        adapter = TypeAdapter(SpotifyUserURI)
        result = adapter.validate_python("  spotify:user:AaBbCcDdEeFfGgHhIiJjKk  ")
        assert result == "spotify:user:AaBbCcDdEeFfGgHhIiJjKk"

    def test_user_uri_invalid_type(self):
        """Test that user URI with wrong type fails."""
        adapter = TypeAdapter(SpotifyUserURI)
        with pytest.raises(ValidationError):
            adapter.validate_python("spotify:track:AaBbCcDdEeFfGgHhIiJjKk")

    def test_user_uri_empty_id(self):
        """Test valid user URI with empty ID."""
        adapter = TypeAdapter(SpotifyUserURI)
        result = adapter.validate_python("spotify:user:")
        assert result == "spotify:user:"
