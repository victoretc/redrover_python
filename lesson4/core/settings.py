from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    base_url: str
    register_password: str


settings = Settings()
# settings = Settings(base_url="http://195.133.27.184/", register_password="Pknewbkj1212234112****")
