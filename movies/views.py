from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *


@api_view(['GET'])
def getMovies(request):
    serializer = MovieSerializer(movie.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMoviesDetails(request, id):
    serializer = MovieSerializer(movie.objects.get(pk=id), many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addMovies(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateMovies(request, id):
    movie_data = movie.objects.get(pk=id)
    serializer = MovieSerializer(instance=movie_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteMovies(request, id):
    movie_data = movie.objects.get(pk=id)
    serializer = MovieSerializer(instance=movie_data, data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response(serializer.data)
