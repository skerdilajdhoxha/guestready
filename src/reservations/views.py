from django.shortcuts import render

from .models import Reservation


def previous_reservations(request):
    all_reservations = Reservation.objects.all().select_related("rental")
    return render(
        request,
        "reservations.html",
        context={"reservations": all_reservations},
    )
