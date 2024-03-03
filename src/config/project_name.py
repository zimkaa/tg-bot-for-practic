import sys

import tomllib


def get_name() -> str:
    with open("pyproject.toml", "rb") as f:  # noqa: PTH123
        data = tomllib.load(f)
    return data["tool"]["poetry"]["name"]


def main() -> None:
    sys.stdout.write(f"{get_name()}\n")


if __name__ == "__main__":
    main()
