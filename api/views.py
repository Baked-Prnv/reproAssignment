from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, timedelta
from .models import Rooms, Booking, UnavailableRoom
from .serializers import  BookingSerializers


# Create your views here.
class CreateBooking(APIView):
    serializer_class = BookingSerializers

    def post(self,req):
        try:
            c_in, c_out = req.data.get("check_in"), req.data.get("check_out")
            allowed_till = date.today() + timedelta(days=6*30)
            if c_in <= date.today() or c_in > allowed_till:
                return Response({"msg":"booking is only allowed from today to 6 months advance..."})
            res = CheckAvailability(req)
            if res["available"]:
                new_booking = Booking.objects.get_or_create(room_id = res["room_id"])
                new_booking["check_in"] = c_in,
                new_booking["check_out"] = c_out,
                new_booking["guest_name"] = req.data.get('guest_name'),
                new_booking.save(update_fields = ['check_in','check_out','guest_name'])
                return Response({"booking_id":new_booking.id,"msg":"booking confirmed"})
            return Response({"msg":"specified room unavailable on the dates"})
        except Exception as e:
            return Response(e)
        

class CheckAvailability(APIView):
    serializer_class = BookingSerializers

    def get(self,req):
        try:
            c_in, c_out, room = req.data.get("check_in",None), req.data.get("check_out",None), req.data.get("room",None)
            print(c_in,c_out,room)
            if c_in and room:
                room_ids = Rooms.objects.filter(room_type = room)
                print(room_ids)
                if c_out:
                    upComingBooking = UnavailableRoom.objects.filter(unavailable_dates__gt=c_in)
                    print(upComingBooking)
                    if upComingBooking.unavailable_dates > c_out:
                        return Response({"available":True, "msg":"we've room available from "+{c_in}+" to "+{c_out}+" in "+{room}})
                    return Response({"available":False, "msg":"we're booked from "+{c_in}+" to "+{c_out}+" in "+{room}})

                if UnavailableRoom.objects.filter(room_id=room_ids).filter(unavailable_dates=c_in):
                    return Response({"available":False, "msg":"room is booked"})
                upComingBooking = UnavailableRoom.objects.get(unavailable_dates__gt=c_in)
                vacant_till = upComingBooking.unavailable_dates - timedelta(days=1)
                return Response({"available":True, "msg":"room is available from "+{c_in}+ " to "+{vacant_till}})
        except Exception as e:
            return Response(e)

class BookingDetails(APIView):
    serializer_class = BookingSerializers

    def get(self,req):
        try:
            booking_id = req.data.get('id',None)
            if booking_id:
                details = Booking.objects.get(id=booking_id)
                return Response({"booking_id":booking_id, 
                                "room_type":details.room_id.room_type, 
                                "check_in":details.check_in,
                                "check_out":details.check_out,
                                "guest_name":details.guest_name})
            return Response({"bad request":"Invalid id given"})
        except Exception as e:
            return Response(e)