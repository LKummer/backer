"""Application Integration Tests"""

from zipfile import Path as ZipPath

from os import system


class TestIntegration:
    """Test module integration."""

    def test_first_run(self, tmp_path):
        """When no backups folder or config are found, they are created."""
        result = system(
            f'poetry run backer tests/data/files -o "{tmp_path}" -r tests/data/files'
        )
        assert result == 0
        # Check the created configuration.
        config = tmp_path.joinpath(".backerrc")
        assert config.exists()
        config_text = config.open("r").read()
        assert config_text == '{"count": 3}'
        # Check the created archive.
        archives = list(tmp_path.glob("*.zip"))
        assert len(archives) == 1
        if archives:
            zip_file = ZipPath(archives[0])
            assert zip_file.joinpath("file_a.md").exists()
            assert zip_file.joinpath("file_b.md").exists()
            assert zip_file.joinpath("file_c.md").exists()
