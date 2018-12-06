from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from inventory.models import Slot
from inventory.serializers import SlotSerializer


class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all().order_by('id')
    serializer_class = SlotSerializer
