from .models import Collection, Card
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CollectionSerializer, CardSerializer



# collection endpoints
class CollectionMethods(APIView):

    def get(self, request):
        #TODO build method to return all collections
        pass

    def post(self, request):
        # TODO build method to create new collection
        pass


# Card endpoints
class CardCollectionMethods(APIView):
    def get(self, request, collection_id):
        # TODO build method to return all cards in a collections
        pass

    def post(self,request,collection_id):
        # TODO build method to create a new card within a collections
        pass


class CardMethods(APIView):

    def put(self, request, collection_id, card_id):
        pass
    # TODO build method to edit an existing card

    def delete(self, request, collection_id, card_id):
        pass
    # TODO build method to delete a card