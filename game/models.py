from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """
    @class Game
    @brief
        Game Model, associate all game related models
    """
    user = models.OneToOneField(User, related_name='game', on_delete=models.CASCADE)
    map = models.OneToOneField('Map',
                               related_name='game',
                               on_delete=models.CASCADE)


class Map(models.Model):
    """
    @class Map
    @brief
        Map Model, associate all game related models
    """


class Cell(models.Model):
    """
    @class Cell
    @brief
        Cell Model, basic elements of a map
    """
    UNDEFINED = 0
    NORMAL = 1
    FARM = 2
    DEPRECATED = 3
    RIVER = 4
    TREE = 5
    CELL_TYPE = (
        (UNDEFINED, 'Undefined'),
        (NORMAL, 'Normal'),
        (FARM, 'Farm'),
        (DEPRECATED, 'Deprecated'),
        (RIVER, 'River'),
        (TREE, 'Tree'),
    )

    position_x = models.IntegerField()
    position_y = models.IntegerField()
    type = models.IntegerField(default=UNDEFINED, choices=CELL_TYPE)
    crop = models.OneToOneField('Crop', related_name='cells', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cell'
        unique_together = ('position_x', 'position_y')


class Crop(models.Model):
    """
    @class Crop
    @brief
        Crop Model, real instance of CropSpecies
    """
    UNDEFINED = 0
    GROWING = 1
    RIPENING = 2
    DEAD = 3
    STATUS_OPTIONS = (
        (UNDEFINED, 'Undefined'),
        (GROWING, 'Growing'),
        (RIPENING, 'Ripening'),
        (DEAD, 'Dead'),
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(default=UNDEFINED, choices=STATUS_OPTIONS)
    ripening_age = models.IntegerField(default=100)
    growing_speed = models.FloatField(default=1.0)  # age add 1.0 per second

    crop_species = models.ForeignKey('CropSpecies', related_name='crops', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Plan'
        ordering = ['-created_at']


class CropSpecies(models.Model):
    """
    @class CropSpecies
    @brief
        CropSpecies Model
    """
    base_ripening_age = models.IntegerField(default=100)
    base_growing_speed = models.FloatField(default=1.0)

    reward_choices = models.ManyToManyField(related_name='crop_species', to='game.Item', through='CropSpeciesRewardDetail')


class Item(models.Model):
    """
    @class Item
    @brief
        Item Model
    """
    prototype = models.ForeignKey('ItemPrototype', related_name='items', on_delete=models.CASCADE)




class ItemPrototype(models.Model):
    """
    @class ItemPrototype
    @brief
        ItemPrototype Model
    """
    UNDEFINED = 0
    SEED = 1
    RESOURCE = 2
    KIT = 3
    TYPE_OPTIONS = (
        (UNDEFINED, 'Undefined'),
        (SEED, 'Seed'),
        (RESOURCE, 'Resource'),
        (KIT, 'Kit'),
    )
    name = models.CharField(max_length=40, unique=False)
    code = models.CharField(max_length=40, unique=True)
    type = models.IntegerField(default=UNDEFINED, choices=TYPE_OPTIONS)


class CropSpeciesRewardDetail(models.Model):
    crop_species = models.ForeignKey('CropSpecies',
                                     related_name='reward_cropses',
                                     on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    weight = models.IntegerField(default=1)

    class Meta:
        unique_together = ('crop_species', 'item')
