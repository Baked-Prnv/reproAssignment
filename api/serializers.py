from rest_framework import serializers
from .models import Rooms, Booking


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id','room','check_in','check_out','guest_name')