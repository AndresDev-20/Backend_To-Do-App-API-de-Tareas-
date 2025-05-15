from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME:str = "To_Do-App"
    PROJECT_VERSION: str = '0.0.1'
    DATABASE_URL:str

    class Config:
        env_file = '.env'

settings = Settings()