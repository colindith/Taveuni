import logging

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, filters
from django.db.models import Max, F
from django.utils import timezone
from django.core.cache import cache

from game.models import Crop, CropSpecies
from game.serializers.serializers import CropSerializer


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer



