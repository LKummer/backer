"""Application Integration Tests"""

from zipfile import Path as ZipPath

from os import system

from backer import CONFIG_NAME


class TestIntegration:
    """Test module integration."""

    def test_first_run(self, tmp_path):
        """When no backups folder or config are found, they are created."""
        result = system(
            f'poetry run backer tests/data/files -o "{tmp_path}" -r tests/data/files'
        )
        assert result == 0
        # Check the created configuration.
        config = tmp_path.joinpath(CONFIG_NAME)
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

    def test_cycling_and_config_loading(self, tmp_path):
        """Config loading is working and archives are correctly cycled."""
        tmp_path.joinpath("first.backer.zip").open("w").close()
        tmp_path.joinpath("second.backer.zip").open("w").close()
        tmp_path.joinpath("third.backer.zip").open("w").close()
        config = tmp_path.joinpath(CONFIG_NAME).open("w")
        config.write('{"count": 1}')
        config.close()
        # Execute the program with a different file count to check it is replaced
        # by the configuration.
        result = system(f'poetry run backer tests/data/files -o "{tmp_path}" -c 5')
        assert result == 0
        # Check only one archive was kept, which means the config was loaded
        # correctly.
        archives = list(tmp_path.glob("*.zip"))
        assert len(archives) == 1
