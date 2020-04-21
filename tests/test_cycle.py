"""Cycle module tests.
"""

from pathlib import Path

from backer.cycle import keep_latest_backups


class TestBackupCycling:
    """Test the backup cycling functionality."""

    def test_basic_cycling(self, tmp_path):
        """Basic cycling functionality works."""
        # Create test files.
        first = tmp_path.joinpath("first.bak.zip")
        first.open("w").close()
        second = tmp_path.joinpath("second.bak.zip")
        second.open("w").close()
        # Cycle the files.
        keep_latest_backups(tmp_path, "*.bak.zip", 1)
        # Check only the one created last still exists.
        assert not first.exists()
        assert second.exists()

    def test_nothing_to_delete(self, tmp_path):
        """No error thrown when nothing needs to be deleted."""
        # Create test file.
        single = tmp_path.joinpath("single.bak.zip")
        single.open("w").close()
        keep_latest_backups(tmp_path, "*.bak.zip", 3)
        # Check it still exists.
        assert single.exists()

    def test_no_backups(self, tmp_path):
        """No error thrown when no backups are found."""
        keep_latest_backups(tmp_path, "*.bak.zip", 1)
