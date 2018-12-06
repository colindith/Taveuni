from rest_framework import serializers
from inventory.models import Slot
from item.serializers import ItemSerializer


class SlotSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Slot
        fields = '__all__'
