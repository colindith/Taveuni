from django.db import models


class Item(models.Model):
    """
    @class Item
    @brief
        Item Model, Real Item Instances
    """
    prototype = models.ForeignKey('ItemPrototype', related_name='items', on_delete=models.CASCADE)


class ItemPrototype(models.Model):
    """
    @class ItemPrototype
    @brief
        ItemPrototype Model, Act As A Template For Real Item Creation
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
    code = models.CharField(max_length=40, unique=True)
    type = models.IntegerField(default=UNDEFINED, choices=TYPE_OPTIONS)
    store_price = models.IntegerField(default=2)
    sold_price = models.IntegerField(default=1)
