from django.db import models
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(max_length=12, default=STATUS_PENDING)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, blank=True, null=True
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

