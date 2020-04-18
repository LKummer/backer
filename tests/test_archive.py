"""Archive module tests.
"""

from pathlib import Path
from zipfile import Path as ZipPath

from pytest import fixture

from backer.archive import archive_files


@fixture
def data_path():
    return Path("./tests/data")


class TestFileArchiving:
    def test_multiple_files(self, data_path, tmp_path):
        files = [
            data_path.joinpath("/files/file_a.md"),
            data_path.joinpath("/files/file_b.md"),
            data_path.joinpath("/files/file_c.md"),
        ]
        root = data_path.joinpath("/files")
        result = tmp_path.joinpath("/multiple_file.zip")
        archive_files(files, root, result)
        assert result.exists()
        # Check to avoid errors when the zip file does not exist.
        if result.exists():
            archive = ZipPath(result)
            # Check that the files exist inside the archive.
            assert archive.joinpath("/file_a.md").exists()
            assert archive.joinpath("/file_b.md").exists()
            assert archive.joinpath("/file_c.md").exists()

    def test_folder(self, data_path, tmp_path):
        files = [data_path.joinpath("/files")]
        result = tmp_path.joinpath("/folder.zip")
        archive_files(files, data_path, result)
        assert result.exists()
        # Check to avoid errors when the zip file does not exist.
        if result.exists():
            archive = ZipPath(result)
            # Check that the files exist inside the archive.
            assert archive.joinpath("/files/file_a.md").exists()
            assert archive.joinpath("/files/file_b.md").exists()
            assert archive.joinpath("/files/file_c.md").exists()

    def test_nested_files(self, data_path, tmp_path):
        files = [data_path.joinpath("/nested/some/nested/folder/nested.md")]
        root = data_path.joinpath("/nested")
        result = tmp_path.joinpath("/nested.zip")
        archive_files(files, root, result)
        assert result.exists()
        # Check to avoid errors when the zip file does not exist.
        if result.exists():
            archive = ZipPath(result)
            # Check that the file exists inside the archive.
            assert archive.joinpath("/some/nested/folder/nested.md").exists()
