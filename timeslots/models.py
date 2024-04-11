from django.db import models
from activities.models import Activity


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

    def save(self, *args, **kwargs):
        if self.available_capacity in [None, '']:
            if self.activity:
                self.available_capacity = self.activity.capacity

        super().save(*args, **kwargs)

# Add a notes section in the model above which will translate to be
# 'Description' in the 'modal' of scheduler.
# Add something like this to signals.py:
# @receiver(post_save, sender=Timeslot)
# def add_timeslot_to_scheduler(sender, instance, created, **kwargs):
#     if created:  # Only add to scheduler if the timeslot is newly created
#         # Create a new event in the scheduler
#         event = Event.objects.create(
#             title=instance.title,  # Adjust these fields
#                                      based on your Timeslot model
#             start=instance.start_time,
#             end=instance.end_time,
#             description=instance.description,
#             # Add other fields as needed
#         )
#         # Save the event
#         event.save()
# This will need all the fields in the event model.
# Create rules of daily, weekly, monthly, hourly etc.
        # Allow these options as possible rules
        # Then allow the user to add a end point for the rule


# Practice displaying the calander on a seperate page until it works properly.
        # Make sure urls and views are set up correctly
