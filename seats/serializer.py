from rest_framework import serializers
from users.serializer import *
from movies.serializers import *
from .models import *


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat
        fields = "__all__"


class BookedSeatSerializer(serializers.ModelSerializer):
    # book = SeatSerializer(many=False, read_only=True, allow_null=True)
    # bookmovie = MovieSerializer(many=False, read_only=True, allow_null=True)
    # bookuser = UserSerializer(many=False, read_only=True, allow_null=True)

    class Meta:
        model = bookedseat
        fields = "__all__"
