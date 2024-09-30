
from pydantic import BaseModel
from typing import List

class ProductData(BaseModel):
    symbol: str

class Product(BaseModel):
    name: str
    market_price: str
    product_data: ProductData

class CoinApiResponse(BaseModel):
    products: List[Product]

class CoinResponseData(BaseModel):
    response_data: CoinApiResponse