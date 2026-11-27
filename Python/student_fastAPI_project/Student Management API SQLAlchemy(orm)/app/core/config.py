from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Access the .env file using pydantic-settings"""

    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str
    database_drivername: str
    app_name: str
    app_version: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
