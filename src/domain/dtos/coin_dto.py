from pydantic import BaseModel
from datetime import datetime

class CoinResponseDto(BaseModel):
    coin_name: str
    symbol: str
    coin_price_brl: float
    date_consult: datetime

class CoinRequestDto(BaseModel):
    symbol: str