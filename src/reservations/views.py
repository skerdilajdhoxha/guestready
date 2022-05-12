from django.db.models import OuterRef, Subquery
from django.shortcuts import render

from .models import Reservation


def previous_reservations(request):
    reservations = Reservation.objects.select_related("rental")
    all_reservations = reservations.annotate(
        previous_reservation=Subquery(
            reservations.filter(rental=OuterRef("rental"))
            .exclude(checkout__gte=OuterRef("checkout"))
            .order_by("-checkout")
            .values("id")[:1]
        )
    )
    return render(
        request,
        "reservations.html",
        context={"reservations": all_reservations},
    )
