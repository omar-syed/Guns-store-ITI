# model -------> json #
# from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import serializers
from . models import Gun

# Serializers define the API representation.
class GunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gun
        fields = '__all__'