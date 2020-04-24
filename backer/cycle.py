"""Backup cycling module."""


def keep_latest_backups(folder, archive_glob, count):
    """Delete old backups to keep only the latest backups.

    Args:
        folder (pathlib.Path): Backups folder to search for archives.
        archive_glob (str): Glob used to find archives.
        count (int): Count of backups to keep.
    """
    matches = folder.glob(archive_glob)
    files = [file for file in matches if file.is_file()]
    for file in files:
        if file.is_dir():
            files.remove(file)
    # Sort files by creation date in reverse.
    sorted_files = sorted(files, key=extract_modification_time, reverse=True)
    for file in sorted_files[count:]:
        try:
            file.unlink()
        except FileNotFoundError:
            print("Path is not a file.")


def extract_modification_time(file):
    """Get the modification time of a file in nanoseconds.

    Args:
        file (pathlib.Path): Path to file.

    Returns:
        int: Most recent content modification in nanoseconds.
    """
    return file.stat().st_mtime_ns
