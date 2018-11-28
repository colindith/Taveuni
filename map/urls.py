from django.urls import path, include
from rest_framework import routers

from map.views import seeding, harvest

router = routers.DefaultRouter()
# router.register(r'item', ItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('seeding', seeding),
    path('harvest', harvest),
]
