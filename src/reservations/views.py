from django.shortcuts import render

from .models import Reservation


def previous_reservations(request):
    last_res_by_rental = (
        Reservation.objects.order_by("rental", "-id")
        .distinct("rental")
        .values_list("id", flat=True)
    )
    prev_reservations = Reservation.objects.exclude(pk__in=list(last_res_by_rental))
    return render(
        request,
        "previous_reservations.html",
        context={"reservations": prev_reservations},
    )
