from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Rooms(models.Model):
    ROOM_TYPE = [
        ('Delux','Delux'),
        ('Luxury','Luxury'),
        ('Luxury Suite','Luxury Suite'),
        ('Presidental Suite','Presidental Suite'),
    ]
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE)
    room_no = models.CharField(max_length=10, unique=True)
    room_price = models.IntegerField()

    def __str__(self):
        return f"{self.room_type} - {self.room_no}"


class Booking(models.Model):
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=50)

    def __str__(self):
        return f"You've a booking for {self.room_id.room_no} from {self.check_in} to {self.check_out}"


class UnavailableRoom(models.Model):
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    unavailable_dates = ArrayField(models.DateField())

    def __str__(self):
        return f"Room {self.room_id.room_no} unavailable dates : {self.unavailable_dates}"