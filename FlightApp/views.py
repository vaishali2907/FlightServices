from django.shortcuts import render
from FlightApp.models import Flight, Passenger, Reservation
from FlightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
# from rest_framework import filters
from rest_framework.authentication import TokenAuthentication


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    filter_backends = filters.SearchFilter
    search_fields = ['departure_city', 'arrival_city', 'date0f_departure']

    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    # authentication_classes = {TokenAuthentication}


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    # filter_backends = filters.SearchFilter
    # search_fields = ['first_name', 'last_name']

    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    authentication_classes = {TokenAuthentication}


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departure_city=request.data['departure_city'],
                                    arrival_city=request.data['arrival_city'],
                                    date0f_departure=request.data['date0f_departure'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flight_number'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.last_name = request.data['last_name']
    passenger.middle_name = request.data['middle_name']
    passenger.email = request.data['email']
    passenger.phone_number = request.data['phone_number']
    passenger.save()

    reservation = Reservation()
    reservation.passenger = passenger
    reservation.flight = flight
    reservation.save()
    return Response(status=HTTP_201_CREATED)
