from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *


@api_view(['GET'])
def getUsers(request):
    serializer = UserSerializer(user.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUsersDetails(request, id):
    serializer = UserSerializer(user.objects.get(pk=id), many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addUsers(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateUsers(request, id):
    user_data = user.objects.get(pk=id)
    serializer = UserSerializer(instance=user_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUsers(request, id):
    user_data = user.objects.get(pk=id)
    serializer = UserSerializer(instance=user_data, data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response(serializer.data)
