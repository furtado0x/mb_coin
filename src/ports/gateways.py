from abc import ABC, abstractmethod
from typing import Any

from src.domain.dtos.coin_dto import CoinResponseDto

class CoinGatewayAbstract(ABC):
    """Abstract class for coin price gateways."""

    base_url: str

    @abstractmethod
    async def get_coin_price(self, coin_id:str) -> CoinResponseDto:
        """Retrieve the price of a coin by its identifier."""

    @abstractmethod
    async def _fetch_coin_price(self, coin_id: str) -> dict:
        """Fetch raw coin price data from the API."""

    @abstractmethod
    def _parse_coin_response(self, data: dict) -> CoinResponseDto:
        """Parse raw API response into a coin price DTO."""
