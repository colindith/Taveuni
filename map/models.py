from django.db import models
from game.models import Crop


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
    map = models.ForeignKey(Map, related_name='cells', on_delete=models.CASCADE)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    type = models.IntegerField(default=UNDEFINED, choices=CELL_TYPE)
    crop = models.OneToOneField(Crop, related_name='cell', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Cell'
        unique_together = ('map', 'position_x', 'position_y')

    def __str__(self):
        return f'({self.position_x}, {self.position_y})/{self.crop}'

    def is_blank_cell(self):
        if not self.crop:
            return True
        return False

    def is_availbe_for_harvest(self):
        if self.crop and self.crop.is_rippening():
            return True
        return False
