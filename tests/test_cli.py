"""CLI module tests."""

from pathlib import Path

from pytest import fixture, raises

from backer.cli import get_parser


@fixture
def parser():
    """Fixture for getting the CLI module's argument parser.

    Returns:
        argparse.ArgumentParser: CLI module's argument parser."""
    return get_parser()


class TestArgParsing:
    """Argument Parser Tests."""

    def test_no_args(self, parser):
        """Make sure the application exits when no args are given."""
        with raises(SystemExit):
            parser.parse_args([])

    def test_no_glob(self, parser):
        """Make sure the glob argument is required."""
        with raises(SystemExit):
            parser.parse_args(["-o", "folder"])

    def test_no_output(self, parser):
        """Make sure the output argument is required."""
        with raises(SystemExit):
            parser.parse_args(["*.py"])

    def test_only_required(self, parser):
        """Make sure it works with minimal arguments and parses them correctly."""
        args = parser.parse_args(["*.py", "-o", "folder"])
        assert args.glob
        assert len(args.glob) == 1
        assert isinstance(args.glob[0], str)
        assert args.output
        assert isinstance(args.output, Path)

    def test_all_arguments(self, parser):
        """Make sure it works with maximum arguments and parses them correctly."""
        args = parser.parse_args(["*.py", "-o", "folder", "-r", "."])
        assert args.glob
        assert len(args.glob) == 1
        assert isinstance(args.glob[0], str)
        assert args.output
        assert isinstance(args.output, Path)
        assert args.root
        assert isinstance(args.root, Path)

    def test_output_to_file(self, parser, tmp_path):
        """Output argument should only accept paths to folders."""
        # Create a file.
        file = tmp_path.joinpath("output_file.zip")
        file.open("w").close()
        # Try to use the file as output.
        with raises(SystemExit):
            parser.parse_args(["*.py", "-o", str(file)])
