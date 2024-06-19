import re
import sys

import requests
from colorama import Fore, Style


def is_san_remo_interesting_yet():
    response = requests.get("https://ismilansanremoexcitingyet.com/")

    if response.status_code != 200:
        raise

    interesting_yet = re.search(r"<h2>(Yes|No)</h2>", response.text).group(1).lower()
    return interesting_yet == "yes"


def main():
    interesting_yet = is_san_remo_interesting_yet()

    if interesting_yet:
        print(f"{Fore.GREEN}✅ finally (almost sounds like a bug!){Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}❌ what did you expect?{Style.RESET_ALL}")
        sys.exit(1)
