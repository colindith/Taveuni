from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from inventory.views import SlotViewSet
from item.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)
router.register(r'slot', SlotViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
