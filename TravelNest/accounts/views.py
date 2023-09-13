from django.shortcuts import render, redirect
from .models import Airport, Flight, Train
from . forms import FlightForm
# Create your views here.
def home(request):

    flights = Flight.objects.all()

    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = form
            return render(request, "accounts/index.html", {"form": form})

    else:
        form = FlightForm()

    context = {
        "flights": flights,
        "form": form,
    }
    return render(request, "accounts/index.html", context)