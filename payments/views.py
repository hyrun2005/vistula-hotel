import uuid
from django.shortcuts import redirect, render
from django.http import HttpResponse
from cloudipsp import Api, Checkout
from django.views.decorators.csrf import csrf_exempt
import logging
import os


# Set up logging
logger = logging.getLogger(__name__)

# Mock function to get or create a basket (replace with your implementation)
def get_or_create_basket(request):
    # Example implementation (replace with your logic)
    class Basket:
        def total_price(self):
            return 53.99  # Replace with the actual calculation logic
    return Basket()

@csrf_exempt
def confirm_order(request):
    """Handles redirecting to Fondy for payment."""
    if request.method != 'POST':
        return HttpResponse("Invalid request method", status=405)

    # Get user basket and calculate total cost
    basket = get_or_create_basket(request)
    total_cost = basket.total_price()

    if total_cost <= 0:
        logger.error("Total cost is zero or negative, cannot proceed with payment.")
        return HttpResponse("Invalid basket total", status=400)

    # Configure Fondy API
    merchant_id = os.getenv("FONDY_MERCHANT_ID", "1396424")  # Use environment variables
    secret_key = os.getenv("FONDY_SECRET_KEY", "test")  # Use environment variables
    api = Api(merchant_id=merchant_id, secret_key=secret_key)
    checkout = Checkout(api=api)

    # Prepare payment data
    data = {
        "currency": "USD",
        "amount": int(float(total_cost) * 100),  # Convert dollars to cents
        "order_id": f"order_{uuid.uuid4().hex}",  # Unique order ID
        "order_desc": "Payment for Vistula order",
        "response_url": request.build_absolute_uri('/payment_success/'),  # Success redirect
        "server_callback_url": request.build_absolute_uri('/payment_callback/'),  # Callback
    }

    try:
        # Generate payment URL
        payment_response = checkout.url(data)
        payment_url = payment_response.get('checkout_url')
        if not payment_url:
            logger.error("Payment URL not returned by Fondy.")
            return HttpResponse("Failed to generate payment URL", status=500)

        logger.info(f"Redirecting to payment URL: {payment_url}")
        return redirect(payment_url)

    except Exception as e:
        logger.exception("Error occurred while generating payment URL.")
        return HttpResponse(f"Error: {e}", status=500)

