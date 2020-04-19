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
## zip_handle is a ZipFile handle.
def add_folder_to_zip(zip_handle, folder_path, zip_root):
    for root, directories, file_names in walk(folder_path):
        for file_name in file_names:
            path = Path(root).joinpath(file_name)
            zip_handle.write(path, path.relative_to(zip_root))
