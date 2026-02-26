from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    database_url: str = Field(..., env='DATABASE_URL')
    secret_key: str = Field(..., env='SECRET_KEY')

    class Config:
        env_file = '.env'

settings = Settings()
