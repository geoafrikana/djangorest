from rest_framework import serializers
from .models import Flight, Passenger, Reservation

class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class passengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
    
    def validate_lastName(self, lastName):
        if lastName.isalpha():
            return lastName.lower()
        else:
            raise serializers.ValidationError('Must contain only alphabets')
        

class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'