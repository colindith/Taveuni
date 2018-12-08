from django.db import models
# from user.models import User


from item.models import Item, ItemPrototype
from game.utils import load_class


# class Game(models.Model):
#     """
#     @class Game
#     @brief
#         Game Model, associate all game related models
#     """
#     user = models.OneToOneField(User, related_name='game', on_delete=models.CASCADE)
#     map = models.OneToOneField(Map,
#                                related_name='game',
#                                on_delete=models.CASCADE)



class CropSpecies(models.Model):
    """
    @class CropSpecies
    @brief
        CropSpecies Model
    """
    name = models.CharField(max_length=40)
    code = models.CharField(primary_key=True, max_length=40)
    base_ripening_age = models.IntegerField(default=100)
    base_growing_speed = models.FloatField(default=1.0)

    reward_choices = models.ManyToManyField(related_name='crop_species', to=ItemPrototype, through='CropSpeciesRewardDetail')
    reward_generator = models.CharField(max_length=255, null=True, blank=True)

    def create_crop(self):
        crop_dict = {
            # 'name': self.name,
            'status': Crop.GROWING,
            'ripening_age': self.base_ripening_age,
            'growing_speed': self.base_growing_speed,
            'age': 0.0,
            'crop_species': self,
        }

        return Crop.objects.create(**crop_dict)


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
    # name = models.CharField(max_length=40)

    status = models.IntegerField(default=UNDEFINED, choices=STATUS_OPTIONS)
    ripening_age = models.IntegerField(default=100)
    growing_speed = models.FloatField(default=1.0)  # age add 1.0 per second
    age = models.FloatField(default=0.0)

    crop_species = models.ForeignKey(CropSpecies, related_name='crops', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.crop_species.name

    def is_rippening(self):
        if self.age > self.ripening_age:
            return True
        return False

    def get_harvest_reward(self):
        # return a list of rewards item objects bur do not delete self
        reward_generator = load_class(self.crop_species.reward_generator)
        if not reward_generator:
            from game.libs.crop_reward_generator import default_generator
            reward_generator = default_generator
        print(f'self.crop_species.reward_choices: {self.crop_species.reward_choices.all()}')
        return reward_generator(self.crop_species.reward_choices.all())


class CropSpeciesRewardDetail(models.Model):
    crop_species = models.ForeignKey(CropSpecies,
                                     related_name='reward_cropses',
                                     on_delete=models.CASCADE)
    item_prototype = models.ForeignKey(ItemPrototype, on_delete=models.CASCADE)
    weight = models.IntegerField(default=1)

    class Meta:
        unique_together = ('crop_species', 'item_prototype')