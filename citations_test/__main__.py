from typing import NoReturn
from citations_test import __version__, __prog__


def main() -> NoReturn:
    print(f"{__prog__} version {__version__}")
    print("Hello world!")
