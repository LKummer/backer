"""CLI Argument Parsing Module."""
from argparse import ArgumentParser, Action, ArgumentError
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
        "-o",
        "--output",
        required=True,
        type=Path,
        action=FolderOnlyAction,
        help="Output folder. Required.",
    )
    parser.add_argument(
        "-c",
        "--count",
        default=3,
        type=int,
        help="Count of backups to keep when deleting old archives. Overriden by the configuration. Defaults to 3.",
    )
    parser.add_argument(
        "-r",
        "--root",
        type=Path,
        default=Path("."),
        help="Root of the added files. Defaults to './'.",
    )
    return parser


class FolderOnlyAction(Action):
    """Action that only accepts a pathlib.Path pointing to a folder."""

    def __call__(self, parser, namespace, values, option_string=None):
        """Action call, see argparse.Action documentation for details."""
        if isinstance(values, Path):
            # If the path does not exist, it can be used for a new folder.
            if values.exists() and not values.is_dir():
                raise ArgumentError(self, "Path must point to a folder.")
            setattr(namespace, self.dest, values)
