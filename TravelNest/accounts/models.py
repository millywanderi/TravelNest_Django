from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=50)
    airportCode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.airportCode}"


class BaseModel(models.Model):
    duration = models.IntegerField()
    arrivalTime = models.DateTimeField(auto_now_add=True)
    departureTime = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    passenger = models.ManyToManyField(User, on_delete=models.CASCADE)

    class Meta:
        abstract=True # no class willl be created


FLIGHT_STATUS =[
    ("Cancelled", "CANCELLED"),
    ("Delayed", "DELAYED"),
    ("On Time", "ON_TIME")
]



class Flight(BaseModel):
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_destination")
    status = models.CharField(blank=True, null=True, max_length=9, choices=FLIGHT_STATUS)
    pointOfDeparture = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_time")

    class Meta:
        ordering = ("pointOfDeparture", "arrivalTime", "departureTime", "destination",)

    def __str__(self):
        return f"{self.pointOfDeparture}, {self.destination}, {self.arrivalTime}"
    
class Train(BaseModel):
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="train_destination")
    status = models.CharField(blank=True, null=True, max_length=9, choices=FLIGHT_STATUS)
    pointOfDeparture = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="train_time")


    def __str__(self):
        return f"{self.pointOfDeparture}, {self.destination}"