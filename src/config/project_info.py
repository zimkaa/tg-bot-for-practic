from pathlib import Path

import tomllib


def get_name() -> str:
    with Path("pyproject.toml").open("rb") as f:
        data = tomllib.load(f)
    return data["tool"]["poetry"]["name"]


def get_version() -> str:
    with Path("pyproject.toml").open("rb") as f:
        data = tomllib.load(f)
    return data["tool"]["poetry"]["version"]
