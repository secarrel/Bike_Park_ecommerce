from django.db import models
from activities.models import Activity
from django.utils import timezone


class Timeslot(models.Model):
    activity = models.ForeignKey(
        Activity,
        related_name='timeslot',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    available_capacity = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    spaces_booked = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return f"{self.activity} - {self.start_time.strftime(
            '%d/%m/%Y @ %H:%M')}"

    def is_future_timeslot(self):
        """
        Check if the start time of the timeslot is in the future.
        Returns True if the start time is in the future and False otherwise.
        """
        return self.start_time > timezone.now()

    def save(self, *args, **kwargs):
        if self.available_capacity in [None, '']:
            if self.activity:
                self.available_capacity = self.activity.capacity

        super().save(*args, **kwargs)
