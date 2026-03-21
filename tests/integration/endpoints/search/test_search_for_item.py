import pytest

from spotantic.endpoints.search import search_for_item
from spotantic.models.search.requests import SearchForItemRequest
from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel
from spotantic.models.spotify import SimplifiedEpisodeModel
from spotantic.models.spotify import SimplifiedShowModel
from spotantic.models.spotify import TrackModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_search_for_item(client):
    # NOTE: Playlist search is currently excluded from this test because the search results contain None values
    # returned by the Spotify API, which causes the test to fail. This against the API documentation,
    # which does not indicate that None values can be returned for playlists.
    result = await search_for_item(
        client,
        query="JENNIE",
        item_type=[
            SpotifyItemType.ALBUM,
            SpotifyItemType.ARTIST,
            SpotifyItemType.EPISODE,
            # SpotifyItemType.PLAYLIST,
            SpotifyItemType.SHOW,
            SpotifyItemType.TRACK,
        ],
        limit=10,
    )

    assert isinstance(result.request, SearchForItemRequest)
    assert isinstance(result.response, dict)

    assert isinstance(result.data.albums, PagedResultModel)
    assert all(isinstance(item, SimplifiedAlbumModel) for item in result.data.albums.items)

    assert isinstance(result.data.artists, PagedResultModel)
    assert all(isinstance(item, ArtistModel) for item in result.data.artists.items)

    assert isinstance(result.data.episodes, PagedResultModel)
    assert all(isinstance(item, SimplifiedEpisodeModel) for item in result.data.episodes.items)

    # assert isinstance(result.data.playlists, PagedResultModel)
    # assert all(isinstance(item, SimplifiedPlaylistModel) for item in result.data.playlists.items)

    assert isinstance(result.data.shows, PagedResultModel)
    assert all(isinstance(item, SimplifiedShowModel) for item in result.data.shows.items)

    assert isinstance(result.data.tracks, PagedResultModel)
    assert all(isinstance(item, TrackModel) for item in result.data.tracks.items)
