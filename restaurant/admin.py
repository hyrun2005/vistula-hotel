from django.contrib import admin
from .models import Category, Dish, DishPhoto

class DishPhotoInline(admin.TabularInline):
    model = DishPhoto
    extra = 1  # Number of extra blank photo fields to show in the admin

class DishAdmin(admin.ModelAdmin):
    inlines = [DishPhotoInline]

admin.site.register(Category)
admin.site.register(Dish, DishAdmin)
