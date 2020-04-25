"""Application Integration Tests"""

from pathlib import Path
from zipfile import Path as ZipPath

from pytest import fixture

from os import system


@fixture
def data_path():
    """Fixture for getting a path to the tests data folder.

    Returns:
        pathlib.Path: Path to the test data folder.
    """
    return Path("./tests/data")


class TestIntegration:
    """Test module integration."""

    def test_first_run(self, data_path, tmp_path):
        """When no backups folder or config are found, they are created."""
        result = system(
            f'poetry run backer tests/data/files -o "{tmp_path}" -r tests/data/files'
        )
        assert result == 0
        archives = list(tmp_path.glob("*.zip"))
        assert len(archives) == 1
        if archives:
            zip_file = ZipPath(archives[0])
            assert zip_file.joinpath("file_a.md").exists()
            assert zip_file.joinpath("file_b.md").exists()
            assert zip_file.joinpath("file_c.md").exists()
