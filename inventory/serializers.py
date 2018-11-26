from rest_framework import serializers
from inventory.models import Item, ItemPrototype


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
