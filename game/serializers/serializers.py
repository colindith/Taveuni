from rest_framework import serializers

from game.models import Cell


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'
