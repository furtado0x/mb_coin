class CoinPriceNotFoundException(Exception):
    def __init__(self, symbol: str):
        self.message = f"Price for the coin '{symbol}' could not be retrieved."
        super().__init__(self.message)
