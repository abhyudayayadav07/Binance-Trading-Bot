import typer

from validators import *
from orderlogic import OrderManager
from clientlayer import BinanceFuturesClient
from logging_config import setup_logger

app = typer.Typer()


@app.command()
def order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    logger = setup_logger()

    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)

    client = BinanceFuturesClient().get_client()

    manager = OrderManager(
        client,
        logger
    )

    print("\nORDER REQUEST")
    print("-" * 30)
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")

    try:

        if order_type == "MARKET":

            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            if price is None:
                raise ValueError(
                    "Price required for LIMIT order"
                )

            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\nSUCCESS")

        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(
            f"Executed Qty: {response['executedQty']}"
        )

    except Exception as e:

        print(f"\nFAILED: {e}")
        logger.error(str(e))


if __name__ == "__main__":
    app()