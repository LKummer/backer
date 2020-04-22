"""Archiving Command Line App."""

from backer.cli import get_parser


__version__ = "0.1.0"


def run():
    """Run the CLI program."""
    args = get_parser().parse_args()
    print(args)
