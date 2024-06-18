import re
import sys

import requests
from clint.textui import colored, puts


def is_san_remo_interesting_yet():
    response = requests.get("https://ismilansanremoexcitingyet.com/")

    if response.status_code != 200:
        raise

    interesting_yet = re.search(r"<h2>(Yes|No)</h2>", response.text).group(1).lower()
    return interesting_yet == "yes"


def main():
    interesting_yet = is_san_remo_interesting_yet()

    if interesting_yet:
        puts(colored.green("✅ finally (almost sounds like a bug!)"))
    else:
        puts(colored.red("❌ what did you expect?"))
        sys.exit(1)
