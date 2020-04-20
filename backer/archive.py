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
    with ZipFile(output, "a") as my_zip:
        for path in files:
            ## Check if path is file or directory.
            if path.is_dir():
                add_folder_to_zip(my_zip, path, root)
            else:
                my_zip.write(path, path.relative_to(root))
        my_zip.close()


## Add entire folder and its contents to existing Zip file.
## zip is a ZipFile handle.
def add_folder_to_zip(zip, folder, root):
    """Archive a folder recursively into a zip archive."""
    for files_root, _, file_names in walk(folder):
        for file_name in file_names:
            file_path = Path(files_root).joinpath(file_name)
            zip.write(file_path, file_path.relative_to(root))
