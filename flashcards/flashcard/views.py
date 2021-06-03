from .models import Collection, Card
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CollectionSerializer, CardSerializer


# collection endpoints
class CollectionMethods(APIView):

    def get(self, request):
        try:
            collections = Collection.objects.all()
        except ValueError:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# Card endpoints
class CardCollectionMethods(APIView):
    def get(self, request, collection_id):
        try:
            cards = Card.objects.filter(collection_id=collection_id)
        except ValueError:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, collection_id):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CardMethods(APIView):

    def put(self, request, collection_id, card_id):
        pass
    # TODO build method to edit an existing card

    def delete(self, request, collection_id, card_id):
        pass
    # TODO build method to delete a card