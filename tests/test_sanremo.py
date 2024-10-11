import functools
import unittest
from dataclasses import dataclass

import sanremo
from requests.exceptions import RequestException


class TestSanRemo(unittest.TestCase):
    def test_is_san_remo_interesting_yet(self):
        self.assertTrue(sanremo.is_san_remo_interesting_yet("<h2>Yes</h2>"))
        self.assertFalse(sanremo.is_san_remo_interesting_yet("<h2>No</h2>"))

    def test_process(self):
        self.assertEqual(sanremo.process(lambda: "<h2>Yes</h2>").exit_code, 0)
        self.assertEqual(sanremo.process(lambda: "<h2>No</h2>").exit_code, 1)

        def raising_fn():
            raise

        self.assertEqual(sanremo.process(raising_fn).exit_code, 2)

    def test_fetch_website(self):
        @dataclass
        class Response:
            status_code: int
            text: str

            def raise_for_status(self):
                if self.status_code != 200:
                    raise RequestException()

        def fetch(status, text, url):
            self.assertEqual(url, sanremo.URL)
            return Response(status, text)

        self.assertEqual(
            sanremo.fetch_website(get=functools.partial(fetch, 200, "foo")), "foo"
        )

        with self.assertRaises(RequestException):
            sanremo.fetch_website(get=functools.partial(fetch, 404, "bar"))
