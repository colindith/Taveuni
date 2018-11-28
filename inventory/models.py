from django.db import models
from django.contrib.postgres import fields as postgres_fields


class ItemPrototype(models.Model):

    name = models.CharField(max_length=40, unique=False)
    code = models.CharField(max_length=40, unique=False)
    type = models.IntegerField(default='Item.UNDEFINED', choices='Item.TYPE_OPTIONS')
    store_price = models.IntegerField(default=2)
    sold_price = models.IntegerField(default=1)
    display_fields = postgres_fields.JSONField(null=True, blank=True)

    # generator will create and return an item instance accourding to rules
    generator = models.CharField(max_length=255, null=True, blank=True)
    rules = postgres_fields.JSONField(null=True, blank=True)

    def generate_item(self):
        # return a Item objects if success, else False
        from game.utils import load_class
        generator = load_class(self.generator)
        return generator(**self.rules)


class Item(models.Model):
    """
    @class Item
    @brief
        Item Model, Real Item Instances
    """

    UNDEFINED = 0
    SEED = 1
    RESOURCE = 2
    KIT = 3
    FRUIT = 4
    TYPE_OPTIONS = (
        (UNDEFINED, 'Undefined'),
        (SEED, 'Seed'),
        (RESOURCE, 'Resource'),
        (KIT, 'Kit'),
        (FRUIT, 'fruit'),
    )

    name = models.CharField(max_length=40, unique=False)
    code = models.CharField(max_length=40, unique=False)
    type = models.IntegerField(default=UNDEFINED, choices=TYPE_OPTIONS)
    store_price = models.IntegerField(default=2)
    sold_price = models.IntegerField(default=1)
    # prototype = models.ForeignKey(ItemPrototype, related_name='items', on_delete=models.CASCADE)
    values = postgres_fields.JSONField(null=True, blank=True)


class SeedItem(Item):
    crop_species = models.ForeignKey('CropSpecies', on_delete=models.CASCADE)


class Inventory(models.Model):
    UNDEFINED = 0
    NOT_FULL = 1
    FULL = 2
    STATUS_OPTIONS = (
        (UNDEFINED, 'Undefined'),
        (NOT_FULL, 'Not_full'),
        (FULL, 'Full'),
    )



    max_slot = models.IntegerField(default=8)

    def insert_item(self, item):
        if not isinstance(item, Item):
            return False

        first_blank_slot = self.is_not_full()
        if not first_blank_slot:
            return False
        first_blank_slot.item = item
        first_blank_slot.save()
        return True

    def insert_item_list(self, item_list):
        if not isinstance(item_list, list):
            return False
        while len(item_list) != 0:
            # TODO: Handle the case that bags' full before all the items inserted into it
            item = item_list.pop()
            self.insert_item(item)

    def fetch_item(self, slot: 'Slot'):
        # return Item object if the action success, else False
        if slot not in self.slots:
            return False
        if not slot.item:
            return False
        item = slot.item
        slot.item = None
        return item

    def is_not_full(self):
        # return False if there is no blank slot, else return the first blank slot
        first_blank_slot = self.slots.all().filter(item__isnull=True).order_by(id).first()
        if first_blank_slot:
            return first_blank_slot
        return False


class Slot(models.Model):
    inventory = models.ForeignKey(Inventory, related_name='slots', on_delete=models.CASCADE)
    item = models.OneToOneField(Item, related_name='slot', blank=True, null=True,
                                on_delete=models.CASCADE)


