"""Backup cycling module."""


def keep_latest_backups(folder, archive_glob, count):
    """Delete old backups to keep only the latest backups.

    Args:
        folder (pathlib.Path): Backups folder to search for archives.
        archive_glob (str): Glob used to find archives.
        count (int): Count of backups to keep.
    """
