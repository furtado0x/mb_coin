from src.domain.exceptions.coin_price_exception import CoinPriceNotFoundException
from src.ports.cache import CacheAbstract
from src.ports.gateways import CoinGatewayAbstract
from src.domain.dtos.coin_dto import CoinResponseDto


class GetCoinPriceUseCase:
    def __init__(
        self,
        gateway: CoinGatewayAbstract,
        fallback_gateway: CoinGatewayAbstract,
        cache: CacheAbstract
    ):
        self.gateway = gateway
        self.fallback_gateway = fallback_gateway
        self.cache = cache

    async def execute(self, symbol: str) -> CoinResponseDto:
        if cached_value := await self.cache.get(key=symbol):
            return cached_value

        try:
            response = await self.gateway.get_coin_price(coin_id=symbol)
        except Exception as e:
            response = await self.fallback_gateway.get_coin_price(
                coin_id=symbol
            )
        if not response:
            raise CoinPriceNotFoundException(symbol=symbol)
        await self.cache.set(key=symbol, value=response.model_dump(mode="json"))
        return response
        