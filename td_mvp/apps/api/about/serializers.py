from rest_framework import serializers

from td_mvp.apps.about.models import Geo, About


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'log']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['name', 'value', 'position']
