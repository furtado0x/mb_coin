from datetime import datetime

import httpx

from .schemas import CoinResponseData
from config import settings
from src.domain.dtos.coin_dto import CoinResponseDto
from src.ports.gateways import CoinGatewayAbstract


class MbGateway(CoinGatewayAbstract):
    base_url = settings.url_mb_gateway

    async def get_coin_price(self, coin_id:str) -> CoinResponseDto:
        coin_data = await self._fetch_coin_price(coin_id=coin_id)
        return self._parse_coin_response(data=coin_data)

    async def _fetch_coin_price(self, coin_id: str) -> dict:
        params = {
            "symbol": coin_id,
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/api/v1/marketplace/product/unlogged",
                    params=params,
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception("Gateway Falied")
            
    def _parse_coin_response(self, data: dict) -> CoinResponseDto | None:
        validated_data = CoinResponseData.model_validate(data)

        product = next(iter(validated_data.response_data.products))
        
        return CoinResponseDto(
            coin_name=product.name,
            symbol=product.product_data.symbol,
            coin_price_brl=float(product.market_price),
            date_consult=datetime.now()
        )
