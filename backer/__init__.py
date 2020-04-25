"""Archiving Command Line App."""

import logging
from pathlib import Path

from backer.cli import get_parser
from backer.config import parse_config, serialize_config
from backer.archive import archive_files
from backer.cycle import keep_latest_backups


__version__ = "0.1.0"


def run():
    """Run the CLI program."""
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("backer")

    args = get_parser().parse_args()
    logger.debug(f"Command line arguments parsed: {args}.")

    # Create the output directory if it does not exist.
    if not args.output.exists():
        logger.debug(f"Output directory does not exist. Creating {args.output}.")
        args.output.mkdir(parents=True)

    # Create the default configuration.
    config = {"count": args.count}

    # Read the output config file, or create a new one it it does not exist.
    config_path = args.output.joinpath(".backerrc")
    if config_path.exists():
        config_text = config_path.open("r").read()
        config = parse_config(config_text)
        logger.debug(f"Config file found. Parsed to {config}")
    else:
        # Save the configuration to file because it does not exist.
        logger.debug(f"Config file does not exist. Writing {config_path}.")
        config_text = serialize_config(config)
        config_path.open("w").write(config_text)

    # Perform glob lookups using all glob arguments.
    execution_path = Path(".")
    files_to_archive = list(
        sum(map(lambda glob: list(execution_path.glob(glob)), args.glob), [])
    )
    logger.debug(f"Archiving files: {files_to_archive}.")
    output_archive = args.output.joinpath("archive.backer.zip")
    archive_files(files_to_archive, args.root, output_archive)

    # Delete backups to keep only the configured count.
    keep_latest_backups(args.output, "*.backer.zip", config["count"])
