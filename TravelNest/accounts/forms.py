from .models import Flight, Airport
from django import from 

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        Fields = [
            "arrivalTime",
            "departureTime",
            "duration",
            "price",
            "status",
            "passanger",
            "pointOfDeparture",
            "destination"
        ]