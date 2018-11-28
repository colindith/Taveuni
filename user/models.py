from django.db import models
from django.contrib.auth.models import AbstractUser

from inventory.models import Inventory
from map.models import Map


class User(AbstractUser):
    inventory = models.OneToOneField(Inventory, related_name='user', on_delete=models.SET_NULL)
    map = models.OneToOneField(Map, related_name='user', on_delete=models.SET_NULL)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)