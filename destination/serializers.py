from rest_framework import serializers

from .models import Point, PointImage, City


class PointImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointImage
        fields = ['url']


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ['name', 'city', 'latitude', 'longitude']


class DetailPointSerializer(serializers.ModelSerializer):
    images = PointImageSerializer(many=True, read_only=True)

    class Meta:
        model = Point
        fields = ['name', 'description', 'city', 'latitude', 'longitude',
                  'images']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'latitude', 'longitude']