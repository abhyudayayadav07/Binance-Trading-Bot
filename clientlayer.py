from binance.client import Client
from config import API_KEY, API_SECRET


class BinanceFuturesClient:

    def __init__(self):
        self.client = Client(
            API_KEY,
            API_SECRET
        )

        self.client.FUTURES_URL = (
            "https://demo-fapi.binance.com/fapi"
        )

    def get_client(self):
        return self.client