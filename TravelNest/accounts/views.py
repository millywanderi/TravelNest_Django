from django.shortcuts import render
from .models import Airport, Flight, Train

# Create your views here.
def home(request):

    flights = Flight.objects.all()

    context = {
        "flights": flights,
    }
    return render(request, "accounts/index.html", context)