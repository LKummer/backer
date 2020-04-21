"""Main CLI Entry Point."""
from backer.cli import get_parser


def run():
    args = get_parser().parse_args()
    print(args)


if __name__ == "__main__":
    run()
