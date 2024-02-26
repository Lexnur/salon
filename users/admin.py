from django.contrib import admin

from carts.admin import CartTabAdmin
from carts.models import Cart


inlines = (CartTabAdmin,)
