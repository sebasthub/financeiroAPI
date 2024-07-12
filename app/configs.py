from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token_url: str
    authorization_url: str
    refresh_url: str
    token_certs: str
    database_url: str

    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def get_setings():
    return Settings()
