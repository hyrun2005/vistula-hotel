from django.shortcuts import redirect, render, HttpResponse
from cloudipsp import Api, Checkout
from django.views.decorators.csrf import csrf_exempt
import logging
import uuid
import os
from restaurant.views import get_or_create_basket

logger = logging.getLogger(__name__)

# 1. Confirm Order View
@csrf_exempt
def confirm_order(request):
    """Handles redirecting to Fondy for payment."""
    if request.method != 'POST':
        logger.warning("Invalid request method: Only POST requests are allowed.")
        return HttpResponse("Invalid request method", status=405)

    try:
        # Get user basket and calculate total cost
        basket = get_or_create_basket(request)
        total_cost = basket.total_price()

        if total_cost <= 0:
            logger.error("Total cost is zero or negative. Cannot proceed with payment.")
            return HttpResponse("Invalid basket total", status=400)

        # Configure Fondy API
        merchant_id = os.getenv("FONDY_MERCHANT_ID", "1396424")
        secret_key = os.getenv("FONDY_SECRET_KEY", "test")
        api = Api(merchant_id=merchant_id, secret_key=secret_key)
        checkout = Checkout(api=api)

        # Prepare payment data
        data = {
            "currency": "USD",
            "amount": int(float(total_cost) * 100),  # Convert dollars to cents
            "order_id": f"order_{uuid.uuid4().hex}",
            "order_desc": "Payment for your order",
            "response_url": request.build_absolute_uri('/payment/payment_success/'),  # Success redirect
            "server_callback_url": request.build_absolute_uri('/payment/payment_callback/'),  # Callback
        }

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


@csrf_exempt
def payment_successful(request):
    """Handles successful payment logic."""
    try:
        basket = get_or_create_basket(request)
        logger.info(f"Basket contents: {basket.basket_items.all()}")
        basket.clear_basket()

        return render(request, 'payment_success.html')

    except Exception as e:
        logger.exception("Error processing payment success.")
        return HttpResponse("An error occurred while processing the payment success page.", status=500)


def payment_failed(request):
    """Handles failed payment scenarios."""
    return render(request, 'payment_failed.html', {
        'message': "Your payment was unsuccessful. Please try again.",
    })


@csrf_exempt
def payment_callback(request):
    """Handles server-to-server callback from the payment gateway."""
    if request.method == 'POST':
        try:
            # Process the callback data
            logger.info(f"Received payment callback: {request.body}")
            # Here you can update the order status in your database based on callback data
            return HttpResponse("Callback received", status=200)

        except Exception as e:
            logger.exception("Error processing payment callback.")
            return HttpResponse("Error processing callback", status=500)
    logger.warning("Invalid request method for payment callback.")
    return HttpResponse("Invalid request method", status=405)
