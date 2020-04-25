"""Archiving Command Line App."""

import logging

from backer.cli import get_parser


__version__ = "0.1.0"


def run():
    """Run the CLI program."""
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("backer")

    args = get_parser().parse_args()
    logger.debug(f"Command line arguments parsed: {args}.")
