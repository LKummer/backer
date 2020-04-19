"""Main CLI Entry Point."""
from backer.cli import get_parser

if __name__ == "__main__":
    ARGS = get_parser().parse_args()
    print(ARGS)
