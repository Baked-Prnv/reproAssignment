from rest_framework import serializers
from .models import UnavailableRoom, Booking, Rooms


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model : Rooms
        fields = '__all__'

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'

class UnavailableRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model : UnavailableRoom
        fields = '__all__'

class BookingSerializer(serializers.Serializer):
    room = serializers.CharField(max_length=100)
    check_in =serializers.DateField()
    check_out = serializers.DateField()
    guest_name = serializers.CharField(max_length=100)