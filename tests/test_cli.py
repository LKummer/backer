"""CLI module tests."""

from pathlib import Path

from pytest import fixture, raises

from backer.cli import get_parser


@fixture
def parser():
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
            parser.parse_args(["-o", "file.zip"])

    def test_no_output(self, parser):
        """Make sure the output argument is required."""
        with raises(SystemExit):
            parser.parse_args(["*.py"])

    def test_only_required(self, parser):
        """Make sure it works with minimal arguments and parses them correctly."""
        args = parser.parse_args(["*.py", "-o", "file.zip"])
        assert args.glob
        assert len(args.glob) == 1
        assert isinstance(args.glob[0], str)
        assert args.output
        assert isinstance(args.output, Path)

    def test_all_arguments(self, parser):
        """Make sure it works with maximum arguments and parses them correctly."""
        args = parser.parse_args(["*.py", "-o", "file.zip", "-r", "."])
        assert args.glob
        assert len(args.glob) == 1
        assert isinstance(args.glob[0], str)
        assert args.output
        assert isinstance(args.output, Path)
        assert args.root
        assert isinstance(args.root, Path)
