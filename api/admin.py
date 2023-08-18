from django.contrib import admin
from .models import Rooms, Booking, UnavailableRoom
# Register your models here.
# @admin.register(Rooms)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id','room_type','room_no','room_price')

admin.site.register(Rooms,RoomAdmin)
admin.site.register(Booking)
admin.site.register(UnavailableRoom)