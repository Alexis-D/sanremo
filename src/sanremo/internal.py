import re
from dataclasses import dataclass

import requests
from colorama import Fore, Style

URL = "https://ismilansanremoexcitingyet.com/"


def is_san_remo_interesting_yet(html):
    interesting_yet = re.search(r"<h2>(Yes|No)</h2>", html).group(1).lower()
    return interesting_yet == "yes"


@dataclass(frozen=True)
class SanRemoStatusAndExitCode:
    status_text: str
    exit_code: int


class SanRemoClient:
    def __init__(self, url=URL):
        self.url = url

    def _fetch_website(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def process(self):
        try:
            html = self._fetch_website()
        except Exception:
            return SanRemoStatusAndExitCode(
                f"{Fore.RED}❌ probably not?{Style.RESET_ALL}", 2
            )

        if is_san_remo_interesting_yet(html):
            return SanRemoStatusAndExitCode(
                f"{Fore.GREEN}✅ finally (almost sounds like a bug!){Style.RESET_ALL}",
                0,
            )

        return SanRemoStatusAndExitCode(
            f"{Fore.RED}❌ what did you expect?{Style.RESET_ALL}", 1
        )
