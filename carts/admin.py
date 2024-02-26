from django.contrib import admin

from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user_display', 'product', 'quantity', 'created_timestamp')
    search_fields = ('user',)

    @staticmethod
    def user_display(obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ('user', 'product', 'quantity', 'created_timestamp')
    search_fields = ('user', 'product', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 1
