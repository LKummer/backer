"""Cycle module tests."""

from time import sleep
from backer.cycle import keep_latest_backups

def short_sleep():
    """Sleep for a very short duration.

    Used for delaying file creations.
    """
    sleep(0.0000001)

class TestBackupCycling:
    """Test the backup cycling functionality."""

    def test_basic_cycling(self, tmp_path):
        """Basic cycling functionality works."""
        # Create test files.
        first = tmp_path.joinpath("first.bak.zip")
        first.open("w").close()
        # Sleep between file creations to fix flakiness.
        short_sleep()
        second = tmp_path.joinpath("second.bak.zip")
        second.open("w").close()
        # Cycle the files.
        keep_latest_backups(tmp_path, "*.bak.zip", 1)
        # Check only the one created last still exists.
        assert not first.exists()
        assert second.exists()

    def test_cycling_with_folder(self, tmp_path):
        """Matched folders are ignored"""
        first = tmp_path.joinpath("first.bak.zip")
        first.open("w").close()
        short_sleep()
        # Make a folder before creating a second file.
        folder = tmp_path.joinpath("folder.bak.zip")
        folder.mkdir()
        short_sleep()
        second = tmp_path.joinpath("second.bak.zip")
        second.open("w").close()
        keep_latest_backups(tmp_path, "*.bak.zip", 2)
        # Assert folder is not counted as a backup.
        assert second.exists()
        assert first.exists()

    def test_cycling_with_bad_count(self, tmp_path):
        """
        No error thrown when count is
        bigger then existine files ammount
        """
        first = tmp_path.joinpath("first.bak.zip")
        first.open("w").close()
        short_sleep()
        second = tmp_path.joinpath("first.bak.zip")
        second.open("w").close()
        # Keep 4 files, only 2 exist.
        keep_latest_backups(tmp_path, "*.bak.zip", 4)


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
