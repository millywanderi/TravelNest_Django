from .models import Flight, Airport
from django import forms

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            "duration",
            "price",
            "status",
            "passenger",
            "pointOfDeparture",
            "destination"
        ]