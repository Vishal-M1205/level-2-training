from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os


class Config(BaseSettings):

    app: str
    data_folder: str
    members_file: Path
    memberships_file: Path
    cities: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()

cwd = Path.cwd()
app: str = config.app

data_folder: Path = cwd / config.data_folder

members_file: Path = data_folder / config.members_file

memberships_file: Path = data_folder / config.memberships_file

cities: list[str] = config.cities.split(",")
