from rest_framework import serializers

from map.models import Cell
from game.serializers.serializers import CropSerializer

class CellSerializer(serializers.ModelSerializer):
    crop = CropSerializer()

    class Meta:
        model = Cell
        fields = '__all__'

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        # print(f'ret: {ret}')

        return ret