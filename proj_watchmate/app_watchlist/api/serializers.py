from rest_framework import serializers
from app_watchlist.models import WatchList, StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    """ Serializer For Model StreamPlatform"""
    
    class Meta:
        """ Meta class to define the model"""
        model = StreamPlatform
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    """ Serializer For Model WatchList"""
    
    class Meta:
        """ Meta class to define the model"""
        model = WatchList
        fields = "__all__"

    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance