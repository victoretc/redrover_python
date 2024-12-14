from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsL1(BaseSettings):
    base_url: str = "http://localhost:8000"

    class ConfigDict(SettingsConfigDict):
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = SettingsL1()
