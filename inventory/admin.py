from django.contrib import admin

from inventory.models import ItemPrototype, Item, Inventory, Slot, SeedItem


admin.site.register(Inventory)
admin.site.register(Item)
admin.site.register(SeedItem)
admin.site.register(ItemPrototype)
admin.site.register(Slot)
