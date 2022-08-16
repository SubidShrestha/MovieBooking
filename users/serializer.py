from rest_framework import serializers
from seats.serializer import *
from .models import user


class UserSerializer(serializers.ModelSerializer):
    bookuser = BookedSeatSerializer(many=True, read_only=True, allow_null=True)
    class Meta:
        model = user
        fields = "__all__"
