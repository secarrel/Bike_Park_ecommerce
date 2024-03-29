import uuid

from django.db import models
from django.db.models import Sum

from timeslots.models import Timeslot
from profiles.models import UserProfile

from django_countries.fields import CountryField

class Order(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        default=0
    )
    full_name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    street_address1 = models.CharField(max_length=80, null=True, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False)    
    postcode = models.CharField(max_length=20, null=True, blank=True)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the order total each time a line item is added.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        Overide the original save method to set the order number if it hasn't
        been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.pk}"


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    updated_quantity = models.PositiveIntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.timeslot.activity}"

    def save(self, *args, **kwargs):
        # Get the original quantity before any updates
        original_quantity = self.quantity

        # Calculate lineitem_total based on the original quantity
        activity = self.timeslot.activity
        self.lineitem_total = activity.price * self.updated_quantity

        # Calculate quantity difference
        quantity_difference = self.updated_quantity - original_quantity

        # Update timeslot's available capacity and spaces booked
        if self.timeslot:
            # Decrease available capacity and increase spaces_booked
            self.timeslot.available_capacity -= quantity_difference
            self.timeslot.spaces_booked += quantity_difference
            
            self.timeslot.save()

        # Update quantity to be equal to updated_quantity
        self.quantity = self.updated_quantity

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.timeslot.available_capacity += self.quantity
        self.timeslot.spaces_booked -= self.quantity
        self.timeslot.save()
        super().delete(*args, **kwargs)
