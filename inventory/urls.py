from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from inventory.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'inventory', ItemViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('list', TemplateView.as_view(template_name='article_list.html')),
    path('', include(router.urls))
]
