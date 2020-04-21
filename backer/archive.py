"""File Archiving Module."""
from zipfile import ZipFile
from os import walk
from pathlib import Path


def archive_files(files, root, output):
    """Archive files into a ZIP archive.

    Args:
        files (:obj:`list` of :obj:`pathlib.Path`): List of paths to add to the
            archive.
        root (pathlib.Path): Root of the content added to the archive.
        output (pathlib.Path): Output archive file.
    """
    print("archive_files called with {}, {}, {}.".format(files, root, output))
    ## root is root directory inside the created zip.
    ## Make new Zip file with the required name.
    with ZipFile(output, "a") as zipfile:
        for path in files:
            ## Check if path is file or directory.
            if path.is_dir():
                archive_folder(zipfile, path, root)
            elif path.is_file():
                archive_file(zipfile, path, root)
        zipfile.close()


def archive_folder(zipfile, folder, root):
    """Archive a folder recursively into a zip archive.

    Args:
        zipfile (zipfile.ZipFile): ZIP file to write to.
        folder (pathlib.Path): Folder to add to the archive.
        root (pathlib.Path): Root of the archive relative to the folder.
    """
    for files_root, _, file_names in walk(folder):
        for file_name in file_names:
            file_path = Path(files_root).joinpath(file_name)
            zipfile.write(file_path, file_path.relative_to(root))


def archive_file(zipfile, file, root):
    """Archive a file into a zip archive.

    Args:
        zipfile (zipfile.ZipFile): ZIP file to write to.
        file (pathlib.Path): File to add to the archive.
        root (pathlib.Path): Root of the archive relative to the folder.
    """
    zipfile.write(file, file.relative_to(root))
