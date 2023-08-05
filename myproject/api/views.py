from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers


@api_view(['GET'])
def getData(request):
    # context = {'name': "Rokon",
    #            'age': 25}
    item = Item.objects.all()
    serializer = ItemSerializers(item,many= True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer2 = ItemSerializers(data=request.data)
    if serializer2.is_valid():
        serializer2.save()
    return Response(serializer2.data)

