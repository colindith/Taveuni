from rest_framework import serializers
from django.utils import timezone

from game.models import Crop, CropSpecies


class CropSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropSpecies
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
    crop_species = CropSpeciesSerializer()
    age_left = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Crop
        fields = '__all__'

    def get_age_left(self, instance):
        return None
