import tomllib


def get_name() -> str:
    with open("pyproject.toml", "rb") as f:  # noqa: PTH123
        data = tomllib.load(f)
    return data["tool"]["poetry"]["name"]


def get_version() -> str:
    with open("pyproject.toml", "rb") as f:  # noqa: PTH123
        data = tomllib.load(f)
    return data["tool"]["poetry"]["version"]
