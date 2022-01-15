import re

from rest_framework import serializers
from FlightApp.models import Passenger, Flight, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flight_number(self, flight_number):

        if re.match("^[a-zA-Z0-9]*$", flight_number) is None:
            raise serializers.ValidationError("Invalid Flight Number. Make sure it is Alpha Numeric.")
        return flight_number


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


