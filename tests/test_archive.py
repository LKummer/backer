"""Archive module tests.
"""

from pathlib import Path
from zipfile import Path as ZipPath

from pytest import fixture, raises

from backer.archive import archive_files


@fixture
def data_path():
    return Path("./tests/data")


class TestFileArchiving:
    def test_multiple_files(self, data_path, tmp_path):
        """Files are added correctly."""
        files = [
            data_path.joinpath("files/file_a.md"),
            data_path.joinpath("files/file_b.md"),
            data_path.joinpath("files/file_c.md"),
        ]
        root = data_path.joinpath("files")
        result = tmp_path.joinpath("multiple_file.zip")
        ## Why is root needed if files are absolute path?
        archive_files(files, root, result)
        assert result.exists()
        # Check to avoid errors when the zip file does not exist.
        if result.exists():
            archive = ZipPath(result)
            # Check that the files exist inside the archive.
            assert archive.joinpath("file_a.md").exists()
            assert archive.joinpath("file_b.md").exists()
            assert archive.joinpath("file_c.md").exists()

    def test_folder(self, data_path, tmp_path):
        """Folder paths are added correctly (recursively)"""
        files = [data_path.joinpath("files")]
        result = tmp_path.joinpath("folder.zip")
        archive_files(files, data_path, result)
        assert result.exists()
        # Check to avoid errors when the zip file does not exist.
        if result.exists():
            archive = ZipPath(result)
            # Check that the files exist inside the archive.
            assert archive.joinpath("files/file_a.md").exists()
            assert archive.joinpath("files/file_b.md").exists()
            assert archive.joinpath("files/file_c.md").exists()

    def test_nested_files(self, data_path, tmp_path):
        """Nested folders are added correctly."""
        files = [data_path.joinpath("nested/some/nested/folder/nested.md")]
        root = data_path.joinpath("nested")
        result = tmp_path.joinpath("nested.zip")
        archive_files(files, root, result)
        assert result.exists()
        # Check to avoid errors when the zip file does not exist.
        if result.exists():
            archive = ZipPath(result)
            # Check that the file exists inside the archive.
            assert archive.joinpath("some/nested/folder/nested.md").exists()

    def test_no_files(self, data_path, tmp_path):
        """Archive is not created when no files are given."""
        result = tmp_path.joinpath("empty.zip")
        archive_files([], data_path, result)
        assert not result.exists()

    def test_files_do_not_exist(self, data_path, tmp_path):
        """Files that do not exist are not added to the archive silently."""
        files = [
            data_path.joinpath("files/file_a.md"),
            data_path.joinpath("files/some_file_that_does_not_exist.md"),
        ]
        result = tmp_path.joinpath("do_not_exist.zip")
        archive_files(files, data_path, result)
        # Check to avoid errors when the zip file does not exist.
        assert result.exists()
        if result.exists():
            archive = ZipPath(result)
            assert archive.joinpath("files/file_a.md").exists()
            # Check that the missing file is not inside the archive.
            assert not archive.joinpath(
                "files/some_file_that_does_not_exist.md"
            ).exists()

    def test_root_is_not_in_file_paths(self, data_path, tmp_path):
        """Exception is raised when file paths cannot be made relative to the root path."""
        files = [data_path.joinpath("files/file_a.md")]
        result = tmp_path.joinpath("invalid_root.zip")
        with raises(ValueError):
            archive_files(files, data_path.joinpath('../../'), result)
