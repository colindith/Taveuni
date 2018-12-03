from rest_framework import serializers
from inventory.models import Item, ItemPrototype, Slot


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Slot
        fields = '__all__'
