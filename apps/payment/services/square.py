import uuid
from square.client import Client
import os

client = Client(
    access_token=os.getenv('SQUARE_ACCESS_TOKEN'),
    environment='sandbox')


class SquarePayService():
    @staticmethod
    def create_checkout():
        result = client.checkout.create_checkout(
            location_id = "L0YMA1TR0834B",
            body = {
                "idempotency_key": str(uuid.uuid4()),
                "description": "pagamento teste",
                "order": {
                    "order": {
                        "location_id": "L0YMA1TR0834B",
                        "reference_id": "idForDjangoHere",
                        # "customer_id": "",
                        "line_items": [
                            {
                                "name": "Temaki",
                                "quantity": "2",
                                "note": "japanese food",
                                "base_price_money": {
                                    "amount": 599,
                                    "currency": "USD"
                                }
                            }
                        ]
                    },
                    "idempotency_key": str(uuid.uuid4())
                },
                "source": "notslowfood"
            }
        )

        if result.is_success():
            return result.body
        elif result.is_error():
            return result.errors

