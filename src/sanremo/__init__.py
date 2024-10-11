import re
import sys
from dataclasses import dataclass

import requests
from colorama import Fore, Style

URL = "https://ismilansanremoexcitingyet.com/"


def fetch_website(get=requests.get):
    response = get(URL)
    response.raise_for_status()
    return response.text


def is_san_remo_interesting_yet(html):
    interesting_yet = re.search(r"<h2>(Yes|No)</h2>", html).group(1).lower()
    return interesting_yet == "yes"


@dataclass
class Result:
    status_text: str
    exit_code: int


def process(fetch=fetch_website):
    try:
        html = fetch()
    except Exception:
        return Result(f"{Fore.RED}❌ probably not?{Style.RESET_ALL}", 2)

    interesting_yet = is_san_remo_interesting_yet(html)

    if interesting_yet:
        return Result(
            f"{Fore.GREEN}✅ finally (almost sounds like a bug!){Style.RESET_ALL}", 0
        )

    return Result(f"{Fore.RED}❌ what did you expect?{Style.RESET_ALL}", 1)


def main():
    result = process()
    print(result.status_text)
    sys.exit(result.exit_code)
