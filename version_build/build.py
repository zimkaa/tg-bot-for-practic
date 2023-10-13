from datetime import datetime

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    version: str = "0.0.999"


settings = Settings()


class Build:
    def __init__(self, *, production: bool = False):
        self.production = production
        self.version = settings.version

    @staticmethod
    def _generate_version_code() -> int:
        """Generate version code
        Every 20 seconds increase it by +1

        :return: version code
        :rtype: int
        """
        start_time = "2023-10-13 00:00:00"
        start_dev = datetime.strptime(start_time, TIME_FORMAT)
        current_date = datetime.now()
        difference = current_date - start_dev
        return int(difference.total_seconds() / 20)  # add +1 every 20 seconds

    def _write_to_file(self) -> None:
        with open("version", "w") as file:
            file.write(self.version)

    def write_version_to_file(self) -> None:
        if not self.production:
            version_code = self._generate_version_code()
            build_number = f"-{version_code}"
            self.version = f"{self.version}{build_number}"
        self._write_to_file()

    def get_version_with_prefix(self) -> str:
        if not self.production:
            version_code = self._generate_version_code()
            build_number = f"-{version_code}"
            self.version = f"{self.version}{build_number}"
        return self.version


if __name__ == "__main__":
    import argparse

    text = """
    Create build version with build number.
    """
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument("-production", action="store_true", help="Creates a build version for production")
    args = parser.parse_args()

    build = Build(production=args.production)
    # build.write_version_to_file()
    print(build.get_version_with_prefix())
