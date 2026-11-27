from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str
    app_name: str
    app_version: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
