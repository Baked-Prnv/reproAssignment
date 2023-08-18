from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime, timedelta
from .models import Rooms, Booking, UnavailableRoom
from .serializers import  BookingSerializer, UnavailableRoomSerializer
from django.db.models import Q


def dates_between(start,end):
    date_list=[]
    while start < end:
        date_list.append(start)
        start += timedelta(days=1)
    return date_list

def available_rooms(check_in,check_out,room_type):
    unavailable_rooms = []
    available_rooms=[]
    all_rooms = Rooms.objects.filter(room_type=room_type).values_list('room_id', flat=True)
    print(all_rooms)
    while check_in<check_out:
        unavailable = UnavailableRoom.objects.filter(unavailable_dates__contains=[check_in]).values_list('room_id', flat=True)
        if len(unavailable)>1:
            for i in unavailable:
                unavailable_rooms.append(i)
        unavailable_rooms.append(unavailable)
        check_in += timedelta(days=1)
    print(unavailable_rooms)
    if all(not qs.exists() for qs in unavailable_rooms):
        available_rooms = all_rooms
        return available_rooms
    available_rooms = all_rooms.exclude(pk__in=unavailable_rooms)
    print(available_rooms)
    return available_rooms



# Create your views here.

class CheckAvailability(APIView):

    def get(self,req):
        serializer = BookingSerializer(data=req.data)
        if serializer.is_valid():
            check_in = serializer.validated_data['check_in']
            check_out = serializer.validated_data['check_out']
            room_type = serializer.validated_data['room']
            availablerooms = available_rooms(check_in,check_out,room_type)
            
            return Response({"rooms":availablerooms})
        return Response({"rooms":None})


class CreateBooking(APIView):
        
    def post(self,req):
        serializer = BookingSerializer(data=req.data)
    
        if serializer.is_valid():
            check_in = serializer.validated_data['check_in']
            check_out = serializer.validated_data['check_out']
            room_type = serializer.validated_data['room']
            dates = dates_between(check_in,check_out)
            rooms = available_rooms(check_in,check_out,room_type)
            room_obj = Rooms.objects.get(room_id=rooms[0])

            if rooms:
                new_booking = Booking.objects.create(room_id=room_obj,
                                                    check_in=check_in,
                                                    check_out=check_out,
                                                    guest_name=serializer.validated_data['guest_name'])
                mark_dates_unavailable = UnavailableRoom.objects.create(room_id=room_obj,unavailable_dates=dates)
            else:
                return Response({"msg":"No rooms available"})
            print(new_booking)
            print(mark_dates_unavailable)
            return Response({"booking_id":new_booking.id, "msg":"your booking has been created"})
        return Response(serializer.errors)
        

class BookingDetails(APIView):

    def get(self,req):
        try:
            booking_id = req.data.get('id',None)
            if booking_id:
                details = Booking.objects.get(id=booking_id)
                return Response({"booking_id":booking_id, 
                                "room_type":details.room_id.room_type, 
                                "room_no":details.room_id.room_no, 
                                "check_in":details.check_in,
                                "check_out":details.check_out,
                                "guest_name":details.guest_name})
            return Response({"bad request":"Invalid id given"})
        except Exception as e:
            return Response(e)