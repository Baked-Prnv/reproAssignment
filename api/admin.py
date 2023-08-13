from django.contrib import admin
from .models import Rooms, Booking, UnavailableRoom
# Register your models here.

admin.site.register(Rooms)
admin.site.register(Booking)
admin.site.register(UnavailableRoom)