import datetime

from django.test import TestCase
from django.test.client import Client

from .models import Rental, Reservation


class TaskTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.rentals = Rental.objects.bulk_create(
            [Rental(name="Rental-1"), Rental(name="Rental-2")]
        )
        Reservation.objects.bulk_create(
            [
                Reservation(
                    rental=self.rentals[0],
                    checkin=datetime.date(2022, 11, 11),
                    checkout=datetime.date(2022, 11, 11),
                ),
                Reservation(
                    rental=self.rentals[0],
                    checkin=datetime.date(2022, 11, 11),
                    checkout=datetime.date(2022, 11, 11),
                ),
                Reservation(
                    rental=self.rentals[1],
                    checkin=datetime.date(2022, 2, 20),
                    checkout=datetime.date(2022, 3, 10),
                ),
                Reservation(
                    rental=self.rentals[1],
                    checkin=datetime.date(2022, 11, 11),
                    checkout=datetime.date(2022, 11, 11),
                ),
                Reservation(
                    rental=self.rentals[1],
                    checkin=datetime.date(2022, 1, 20),
                    checkout=datetime.date(2022, 2, 11),
                ),
            ]
        )

    def test_previous_reservations_view(self):
        test_response = self.client.get("/")
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, "reservations.html")

        self.assertEqual(len(test_response.context["reservations"]), 5)
        last_res_by_rental = (
            Reservation.objects.order_by("rental", "-id")
            .distinct("rental")
            .values_list("id", flat=True)
        )
        prev_reservations = Reservation.objects.exclude(pk__in=list(last_res_by_rental))
        self.assertEqual(len(prev_reservations), 3)
