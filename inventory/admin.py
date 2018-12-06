from django.contrib import admin

from inventory.models import Inventory, Slot


admin.site.register(Inventory)
admin.site.register(Slot)
