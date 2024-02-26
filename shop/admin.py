from django.contrib import admin
from shop.models import Categories, Products


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'discount', 'availability')
    list_editable = ('discount', 'availability')
    search_fields = ('name',)
    list_filter = ('name', 'availability', 'category')




