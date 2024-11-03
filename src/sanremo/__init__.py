import sys

from .internal import SanRemoClient


def main():
    client = SanRemoClient()
    result = client.process()
    print(result.status_text)
    sys.exit(result.exit_code)
