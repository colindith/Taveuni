from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from item.models import Item, ItemPrototype
from item.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(['GET', 'POST'])
def sell_item(request):
    user = request.user

    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})