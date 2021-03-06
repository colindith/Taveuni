from django.urls import path, include
from rest_framework import routers

from map.views import seeding, gathering, CellViewSet

router = routers.DefaultRouter()
router.register(r'cell', CellViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('seeding/', seeding),
    path('gathering/', gathering),
]
