from django.db import models
from django.contrib.auth.models import User

# Category model to store different dish categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BasketItem(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, related_name='basket_items')
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.dish.name} ({self.quantity})"


# Dish model with category
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name


# DishPhoto model for storing multiple photos for each dish
class DishPhoto(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='dishes/photos/')

    def __str__(self):
        return f"Photo for {self.dish.name}"

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    items = models.ManyToManyField('Dish', through='BasketItem')

    def total_price(self):
        """Calculates the total price of all items in the basket."""
        return sum(item.dish.price * item.quantity for item in self.basket_items.all())

    def add_item(self, dish):
        """Adds a dish to the basket."""
        basket_item, created = BasketItem.objects.get_or_create(basket=self, dish=dish)
        if not created:
            basket_item.quantity += 1
            basket_item.save()

    def remove_item(self, dish_id):
        """Removes a dish from the basket."""
        BasketItem.objects.filter(basket=self, dish_id=dish_id).delete()

    def clear_basket(self):
        """Clears all items from the basket."""
        self.basket_items.all().delete()
