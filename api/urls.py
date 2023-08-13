from django.urls import path
from .views import CheckAvailability, CreateBooking, BookingDetails

urlpatterns = [
    path('check',CheckAvailability.as_view()),
    path('create',CreateBooking.as_view()),
    path('detail',BookingDetails.as_view()),
]