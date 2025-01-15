from unittest.mock import patch

import pytest
from assertpy import assert_that
from requests.exceptions import RequestException

import sanremo.internal


@pytest.fixture
def client():
    return sanremo.internal.SanRemoClient()


def test_is_san_remo_interesting_yet():
    assert_that(sanremo.internal.is_san_remo_interesting_yet("<h2>Yes</h2>")).is_true()
    assert_that(sanremo.internal.is_san_remo_interesting_yet("<h2>No</h2>")).is_false()


def test_process():
    client = sanremo.internal.SanRemoClient()

    with patch.object(client, "_fetch_website", return_value="<h2>Yes</h2>"):
        assert_that(client.process().exit_code).is_equal_to(0)

    with patch.object(client, "_fetch_website", return_value="<h2>No</h2>"):
        assert_that(client.process().exit_code).is_equal_to(1)

    with patch.object(client, "_fetch_website", side_effect=Exception):
        assert_that(client.process().exit_code).is_equal_to(2)


@patch("requests.get")
def test_fetch_website_when_get_succeeds(mock_get, client):
    mock_get.return_value.text = "foo"

    assert_that(client._fetch_website()).is_equal_to("foo")

    mock_get.assert_called_once_with(sanremo.internal.URL)
    mock_get.return_value.raise_for_status.assert_called_once()


@patch("requests.get")
def test_fetch_website_when_get_succeeds_but_return_error_response(mock_get, client):
    mock_get.return_value.raise_for_status.side_effect = RequestException

    assert_that(client._fetch_website).raises(RequestException).when_called_with()

    mock_get.assert_called_once_with(sanremo.internal.URL)
    mock_get.return_value.raise_for_status.assert_called_once()


@patch("requests.get", side_effect=Exception("error"))
def test_fetch_website_when_get_fails(mock_get, client):
    assert_that(client._fetch_website).raises(Exception).when_called_with().is_equal_to(
        "error"
    )

    mock_get.assert_called_once_with(sanremo.internal.URL)
