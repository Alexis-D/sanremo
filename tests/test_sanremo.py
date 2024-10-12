from unittest.mock import Mock

import requests
import sanremo
from assertpy import assert_that
from requests.exceptions import RequestException


def test_is_san_remo_interesting_yet():
    assert_that(sanremo.is_san_remo_interesting_yet("<h2>Yes</h2>")).is_true()
    assert_that(sanremo.is_san_remo_interesting_yet("<h2>No</h2>")).is_false()


def test_process():
    assert_that(sanremo.process(lambda: "<h2>Yes</h2>").exit_code).is_equal_to(0)
    assert_that(sanremo.process(lambda: "<h2>No</h2>").exit_code).is_equal_to(1)
    assert_that(sanremo.process(Mock(side_effect=Exception)).exit_code).is_equal_to(2)


def test_fetch_website_when_get_succeeds():
    success_reponse = Mock(spec=requests.Response)
    success_reponse.text = "foo"
    get_success = Mock(return_value=success_reponse)
    assert_that(sanremo.fetch_website(get=get_success)).is_equal_to("foo")
    get_success.assert_called_once_with(sanremo.URL)
    success_reponse.raise_for_status.assert_called_once()


def test_fetch_website_when_get_fails():
    failure_response = Mock(spec=requests.Response)
    failure_response.raise_for_status.side_effect = RequestException
    get_failure = Mock(return_value=failure_response)

    assert_that(sanremo.fetch_website).raises(RequestException).when_called_with(
        get=get_failure
    )
    get_failure.assert_called_once_with(sanremo.URL)
    failure_response.raise_for_status.assert_called_once()
