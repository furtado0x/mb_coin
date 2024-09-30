from datetime import datetime

import httpx

from config import settings

from .schemas import CoinResponseData
from src.domain.dtos.coin_dto import CoinResponseDto
from src.ports.gateways import CoinGatewayAbstract


class CoinMarketCapGateway(CoinGatewayAbstract):
    base_url = settings.url_coin_market_cap_gateway

    async def get_coin_price(self, coin_id:str) -> CoinResponseDto:
        coin_data = await self._fetch_coin_price(coin_id=coin_id)
        return self._parse_coin_response(data=coin_data)

    async def _fetch_coin_price(self, coin_id: str) -> dict:
        headers = {
            "X-CMC_PRO_API_KEY": settings.token_coin_market_cap_gateway
        }
        params = {"symbol": coin_id, "convert": "BRL"}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/v1/cryptocurrency/quotes/latest",
                    headers=headers,
                    params=params,
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception("Gateway Falied")
            
    def _parse_coin_response(self, data: dict) -> CoinResponseDto | None:
        validated_data = CoinResponseData.model_validate(data)
        if not validated_data.data:
            return None

        coin_key = next(iter(validated_data.data))
        coin_data = validated_data.data[coin_key]
        
        brl_quote = coin_data.quote["BRL"]

        return CoinResponseDto(
            coin_name=coin_data.name,
            symbol=coin_data.symbol,
            coin_price_brl=brl_quote.price,
            date_consult=datetime.now()
        )
