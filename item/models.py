from django.db import models
from django.contrib.postgres import fields as postgres_fields


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


class ItemPrototype(models.Model):
    # TODO: Item should not be in Inventory app
    name = models.CharField(max_length=40)
    code = models.CharField(primary_key=True, max_length=40)
    type = models.IntegerField(default='Item.UNDEFINED', choices=TYPE_OPTIONS)
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
        if not generator:
            from item.libs.item_generator import default_generator
            generator = default_generator
        if self.rules:
            return generator(item_prototype=self, **self.rules)
        else:
            return generator(item_prototype=self)


class Item(models.Model):
    """
    @class Item
    @brief
        Item Model, Real Item Instances
    """

    name = models.CharField(max_length=40, unique=False, default='none')
    type = models.IntegerField(default=UNDEFINED, choices=TYPE_OPTIONS)
    store_price = models.IntegerField(default=2)
    sold_price = models.IntegerField(default=1)
    # prototype = models.ForeignKey(ItemPrototype, related_name='items', on_delete=models.CASCADE)
    values = postgres_fields.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}/{self.id}'
