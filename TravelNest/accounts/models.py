from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=50)
    airportCode = models.CharField(max_length=50)


class BaseModel(models.Model):
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_destination")
    arrivalTime = models.DateTimeField(auto_now_add=True)
    departureTime = models.DateTimeField(auto_now_add=True)
    pointOfDeparture = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_time")

    class Meta:
        abstract=True # no class willl be created


FLIGHT_STATUS =[
    ("Cancelled", "CANCELLED"),
    ("Delayed", "DELAYED"),
    ("On Time", "ON_TIME")
]


class Flight(BaseModel):
    CANCELLED = "Cancelled",
    DELAYED = "Delayed",
    ON_TIME = "On Time"

    FLIGHT_STATUS =[
        (CANCELLED, "Cancelled"),
        (DELAYED, "Delayed"),
        (ON_TIME, "On Time")
    ]
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=2, default=ON_TIME)

    class Meta:
        ordering = ("pointOfDeparture", "arrivalTime", "departureTime", "destination",)

    def __str__(self):
        return f"{self.pointOfDeparture}, {self.destination}, {self.arrivalTime}"