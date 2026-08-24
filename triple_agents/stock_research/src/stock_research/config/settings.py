from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_api_key: str = Field(
        ...,
        description='Google Gemini API key for LLM'
    )
    alpha_vantage_api_key: str = Field(
        ...,
        description='API key for financial data'
    )

    alpha_vantage_base_url: str = Field(
        ...,
        description='Base url for making an request'
    )

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra='ignore'
    )


settings = Settings()
