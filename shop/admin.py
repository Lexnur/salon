from django.contrib import admin
from shop.models import Categories, Products


# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



