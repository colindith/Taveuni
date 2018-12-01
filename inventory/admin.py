from django.contrib import admin

from inventory.models import ItemPrototype, Item


admin.site.register(Item)
admin.site.register(ItemPrototype)
