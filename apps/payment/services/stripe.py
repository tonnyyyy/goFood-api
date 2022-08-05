import os
from typing import TypedDict
import time
import stripe
stripe.api_key = os.getenv('STRIPE_API_KEY')

class ICreateSessionReturn(TypedDict):
    id: str
    url: str

class StripeService():
    @staticmethod
    def create_checkout_session(currency: str = 'brl') -> ICreateSessionReturn:
        """
            Cria uma página web para realizar o pagamento.\n
            Retorna a URL para a página criada.
        """

        session = stripe.checkout.Session.create(
            line_items = [{
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': 'Temaki'
                    },
                    'unit_amount': 1500 # cents
                },
                'quantity': 2
            }],
            mode='payment',
            success_url='https://google.com',
            cancel_url='https://facebook.com'
        )

        return {
            'id': session.get('id'),
            'url': session.instance_url,
        }

    @staticmethod
    def expire_checkout_session(id: str):
        """
            Expira a sessão da página de pagamento.\n
            id: ID da sessão.
        """

        stripe.checkout.Session.expire(id)

