from rest_framework import serializers
from .models import Collection, Card


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'term', 'definition', 'collection']

    def update(self, instance, validated_data):
        instance.term = validated_data.get('term', instance.term)
        instance.definition = validated_data.get('definition', instance.definition)
        instance.save()
        return instance
