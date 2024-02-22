from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: int
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:123@localhost:5432/SQL2
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        # postgresql+psycopg://postgres:123@localhost:5432/SQL2
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Если захочешь вызвать из IDE, а не из консоли. Используй - "E:\Python courses\sql_alchemy_cours\.env" или "..\.env"
    # Иначе используй ".env"
    model_config = SettingsConfigDict(env_file='..\.env')


settings = Settings()
