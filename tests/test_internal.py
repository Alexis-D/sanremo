from unittest.mock import Mock, patch

import requests
from assertpy import assert_that
from requests.exceptions import RequestException

import sanremo.internal


def test_is_san_remo_interesting_yet():
    assert_that(sanremo.internal.is_san_remo_interesting_yet("<h2>Yes</h2>")).is_true()
    assert_that(sanremo.internal.is_san_remo_interesting_yet("<h2>No</h2>")).is_false()


def test_process():
    with patch("sanremo.internal.fetch_website", return_value="<h2>Yes</h2>"):
        assert_that(sanremo.internal.process().exit_code).is_equal_to(0)

    with patch("sanremo.internal.fetch_website", return_value="<h2>No</h2>"):
        assert_that(sanremo.internal.process().exit_code).is_equal_to(1)

    with patch("sanremo.internal.fetch_website", side_effect=Exception):
        assert_that(sanremo.internal.process().exit_code).is_equal_to(2)


@patch("requests.get")
def test_fetch_website_when_get_succeeds(mock_get):
    success_reponse = Mock(spec=requests.Response)
    success_reponse.text = "foo"
    mock_get.return_value = success_reponse

    assert_that(sanremo.internal.fetch_website()).is_equal_to("foo")

    mock_get.assert_called_once_with(sanremo.internal.URL)
    success_reponse.raise_for_status.assert_called_once()


@patch("requests.get")
def test_fetch_website_when_get_succeeds_but_return_error_response(mock_get):
    failure_response = Mock(spec=requests.Response)
    failure_response.raise_for_status.side_effect = RequestException
    mock_get.return_value = failure_response

    assert_that(sanremo.internal.fetch_website).raises(
        RequestException
    ).when_called_with()

    mock_get.assert_called_once_with(sanremo.internal.URL)
    failure_response.raise_for_status.assert_called_once()


@patch("requests.get", side_effect=Exception("error"))
def test_fetch_website_when_get_fails(mock_get):
    assert_that(sanremo.internal.fetch_website).raises(
        Exception
    ).when_called_with().is_equal_to("error")

    mock_get.assert_called_once_with(sanremo.internal.URL)
