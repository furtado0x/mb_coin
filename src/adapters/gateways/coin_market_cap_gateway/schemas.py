from pydantic import BaseModel
from datetime import datetime

class CoinQuote(BaseModel):
    price: float
    last_updated: datetime

class CoinData(BaseModel):
    name: str
    symbol: str
    quote: dict[str, CoinQuote]

class CoinResponseData(BaseModel):
    status: dict
    data: dict[str, CoinData]