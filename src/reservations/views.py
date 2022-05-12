from django.shortcuts import render

from .models import Reservation


def previous_reservations(request):
    all_reservations = Reservation.objects.all()
    return render(
        request,
        "previous_reservations.html",
        context={"reservations": all_reservations},
    )
