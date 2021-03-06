from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(
        "reservations.Rental", on_delete=models.SET_NULL, null=True
    )
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"{self.id}"
