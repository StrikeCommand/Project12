from rest_framework import serializers

from .models import Point, PointImage, City


class PointImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointImage
        fields = ['id', 'url']


class ListPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ['id', 'name', 'city', 'latitude', 'longitude']


class PointSerializer(serializers.ModelSerializer):
    images = PointImageSerializer(many=True, read_only=True)

    class Meta:
        model = Point
        fields = ['id', 'name', 'description', 'city', 'latitude', 'longitude',
                  'images']


class CitySerializer(serializers.ModelSerializer):
    points = ListPointSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'latitude', 'longitude', 'points']


class ListCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name', 'latitude', 'longitude']