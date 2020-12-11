from django.contrib import admin
from .models import Category, Product

# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'slug','name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['category', 'available', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':('name',)}
