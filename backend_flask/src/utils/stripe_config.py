import stripe
import os

stripe.api_key = os.getenv('STRIPE_API_KEY')

def create_stripe_payment_intent(amount, currency, metadata):
    return stripe.PaymentIntent.create(
        amount=int(amount * 100),  # Convert dollars to cents
        currency=currency,
        metadata=metadata
    )
