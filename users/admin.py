from django.contrib import admin
from django.contrib.auth.models import User

from carts.admin import CartTabAdmin
from users.models import Order, OrderItem


# admin.site.register(Order)
# admin.site.register(OrderItem)


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("product", "name", "price",)
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "name", "price", "created_timestamp")
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "status",
        "payment_on_get",
    )

    search_fields = (
        "payment_on_get",
    )
    readonly_fields = ("created_at",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "status",
        "payment_on_get",
        "payment_on_pay",
        "status",
        "created_at",

    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_at",)
    list_filter = (
        "status",
        "payment_on_get",
    )
    inlines = (OrderItemTabulareAdmin,)


inlines = (CartTabAdmin, OrderTabulareAdmin)















