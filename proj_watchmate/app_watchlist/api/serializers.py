from rest_framework import serializers
from app_watchlist.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    """ Serializer For Model WatchList"""

    reviews = ReviewSerializer(many=True, read_only=True)
    #reviews = ReviewRatingField(many=True, read_only=True)
    class Meta:
        """ Meta class to define the model"""
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    """ Serializer For Model StreamPlatform"""
    watchlist = WatchListSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-detail")
    class Meta:
        """ Meta class to define the model"""
        model = StreamPlatform
        fields = "__all__"





    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance