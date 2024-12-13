from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Dish, Basket



def mainPageRes(request):
    return render(request, 'main_page_res.html', {})


def menu_view(request):
    """Renders the menu page with dishes filtered by category."""
    # Get the category ID from the query parameter
    category_id = request.GET.get('category', 'all')

    if category_id == 'all':
        categories = Category.objects.prefetch_related('dishes__photos').all()
    else:
        categories = Category.objects.prefetch_related('dishes__photos').filter(id=category_id)

    return render(request, 'menu_page.html', {'categories': categories})

def get_or_create_basket(request):
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        basket, created = Basket.objects.get_or_create(session_key=session_key, user=None)
    return basket

def total_price(self):
    """Calculates the total price of all items in the basket."""
    return sum(item.dish.price * item.quantity for item in self.basket_items.all())

def clear_basket(self):
    """Clears all items from the basket."""
    self.basket_items.all().delete()


def set_basket(request, basket):
    """Sets the basket for authenticated or anonymous users."""
    if request.user.is_authenticated:
        request.user.basket = basket
        request.user.save()
    else:
        request.session['basket'] = basket
        request.session.modified = True


# Add item to basket
def add_to_basket(request, dish_id):
    """Adds a dish to the basket."""
    basket = get_or_create_basket(request)  # Use the utility function
    dish = get_object_or_404(Dish, id=dish_id)
    basket.add_item(dish)  # Use the add_item method of the Basket model
    messages.success(request, f"{dish.name} added to basket!")
    return redirect('basket')  # Redirect to the basket page



# Basket view
def basket_view(request):
    """Renders the basket view."""
    basket = get_or_create_basket(request)
    return render(request, 'basket_page.html', {
        'basket': basket.basket_items.all(),  # Pass related BasketItem objects
        'total_price': basket.total_price(),  # Calculate the total price
    })

def delete_from_basket(request, dish_id):
    """Deletes an item from the basket."""
    if request.method == "POST":
        basket = get_or_create_basket(request)  # Use the utility function
        basket.remove_item(dish_id)  # Remove the item using its ID
        messages.success(request, "Item removed from basket.")
    return redirect('basket')  # Redirect back to the basket page



def order_view(request):
    """Handles order placement and clearing the basket."""
    basket = get_or_create_basket(request)
    total_cost = basket.total_price()

    if request.method == 'POST':
        basket.clear_basket()
        messages.success(request, "Order placed successfully!")
        return render(request, 'order_success.html', {'total_cost': total_cost})

    return render(request, 'order_page.html', {
        'basket': basket.basket_items.all(),
        'total_cost': total_cost
    })






