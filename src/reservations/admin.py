from django.contrib import admin

from .models import Rental, Reservation


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["rental", "id", "checkin", "checkout"]
