from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    redis_host: str
    redis_port: int
    redis_ttl: int
    redis_namespace: str

    url_coin_market_cap_gateway: str
    token_coin_market_cap_gateway: str

    url_mb_gateway: str

    class Config:
        env_file = ".env"

settings = Settings()
