from django.contrib import admin

from item.models import ItemPrototype, Item


admin.site.register(Item)
admin.site.register(ItemPrototype)