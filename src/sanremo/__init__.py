import sys

from .internal import process


def main():
    result = process()
    print(result.status_text)
    sys.exit(result.exit_code)
