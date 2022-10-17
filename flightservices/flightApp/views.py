from django.shortcuts import render
from .models import Passenger, Reservation, Flight
from .serializers import flightSerializer, passengerSerializer, reservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def find_flights(request):
    flight = Flight.objects.filter(departureCity=request.data.get('departureCity'), arrivalCity=request.data.get('arrivalCity'), dateOfDeparture=request.data.get('dateOfDeparture'))
    serializer = flightSerializer(flight, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.email=request.data['email']
    passenger.middleName=request.data['middleName']
    passenger.phone=request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight=flight
    reservation.passenger=passenger

    reservation.save()
    return Response(request.data,status=status.HTTP_201_CREATED)




class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = flightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = passengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = reservationSerializer

