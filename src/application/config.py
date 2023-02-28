from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Base Configuration
    """
    TESTING: bool = False
    APP_NAME: str
    ENV: str
    API_VERSION: str
    TITLE: str

    class Config:
        env_file = 'src/.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.ENV}")
    return settings
