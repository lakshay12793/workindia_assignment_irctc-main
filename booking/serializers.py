from rest_framework import serializers
from .models import CustomUser, Train, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'is_admin']

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['source', 'destination', 'total_seats', 'available_seats']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user', 'train', 'seats_booked', 'booking_time']
