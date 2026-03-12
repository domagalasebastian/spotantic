from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.users import get_current_user_profile
from spotantic.models.spotify import CurrentUserModel
from spotantic.models.users.requests import GetCurrentUserProfileRequest


@pytest.mark.asyncio
async def test_get_current_user_profile_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "user123"}
    client.request_json.return_value = fake_response

    request_obj = object()
    user_model = SimpleNamespace(id="user123")

    with (
        mock.patch.object(GetCurrentUserProfileRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(CurrentUserModel, "model_validate", return_value=user_model) as validate_mock,
    ):
        result = await get_current_user_profile(client)

        build_mock.assert_called_once_with()
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is user_model
