from rest_framework import serializers
from .models import *


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class LeadershipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = "__all__"

class RequisitesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requisites
        fields = "__all__"

class OpenDataSerializers(serializers.ModelSerializer):
    class Meta:
        models = OpenData
        fields = "__all__"

class DirectionsSerializers(serializers.ModelSerializer):
    class Meta:
        models = Directions
        fields = "__all__"