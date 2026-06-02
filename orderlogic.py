from binance.exceptions import BinanceAPIException

class OrderManager:

    def __init__(self, client, logger):

        self.client = client
        self.logger = logger

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            self.logger.info(response)

            return response

        except BinanceAPIException as e:

            self.logger.error(str(e))
            raise


    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            self.logger.info(response)

            return response

        except BinanceAPIException as e:

            self.logger.error(str(e))
            raise