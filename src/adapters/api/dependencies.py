from src.adapters.caches.redis_cache import RedisCache
from src.adapters.gateways import MbGateway, CoinMarketCapGateway
from src.domain.usecases.get_coin_price_usecase import GetCoinPriceUseCase


def get_coin_use_case() -> GetCoinPriceUseCase:
    gateway = MbGateway()
    fallback_gateway = CoinMarketCapGateway()
    redis_cache = RedisCache()
    return GetCoinPriceUseCase(
        gateway=gateway,
        fallback_gateway=fallback_gateway,
        cache=redis_cache
    )