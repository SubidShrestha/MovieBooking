from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *


@api_view(['GET'])
def getSeats(request):
    serializer = SeatSerializer(seat.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSeatsDetails(request, id):
    serializer = SeatSerializer(seat.objects.get(pk=id), many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addSeats(request):
    serializer = SeatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateSeats(request, id):
    seat_data = seat.objects.get(pk=id)
    serializer = SeatSerializer(instance=seat_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSeats(request, id):
    seat_data = seat.objects.get(pk=id)
    serializer = SeatSerializer(instance=seat_data, data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response(serializer.data)


@api_view(['GET'])
def getBookedSeats(request):
    serializer = BookedSeatSerializer(bookedseat.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBookedSeatsDetails(request, id):
    serializer = BookedSeatSerializer(
        bookedseat.objects.get(pk=id), many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addBookedSeats(request):
    serializer = BookedSeatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateBookedSeats(request, id):
    seat_data = bookedseat.objects.get(pk=id)
    serializer = BookedSeatSerializer(instance=seat_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBookedSeats(request, id):
    seat_data = bookedseat.objects.get(pk=id)
    serializer = BookedSeatSerializer(instance=seat_data, data=request.data)
    if serializer.is_valid():
        serializer.delete()
    return Response(serializer.data)
