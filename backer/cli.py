"""CLI Argument Parsing Module."""
from argparse import ArgumentParser
from pathlib import Path


def get_parser():
    """Creates a CLI argument parser.

    Returns:
        argparse.ArgumentParser: Argument parser.
    """
    parser = ArgumentParser(description="Create backup archives.")
    parser.add_argument(
        "glob", type=str, nargs="+", help="Glob of files to archive. Required.",
    )
    parser.add_argument(
        "-o", "--output", required=True, type=Path, help="Output zip file. Required."
    )
    parser.add_argument(
        "-r",
        "--root",
        type=Path,
        default=Path("."),
        help="Root of the added files. Defaults to './'.",
    )
    return parser
