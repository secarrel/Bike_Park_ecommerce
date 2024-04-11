from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem

    readonly_fields = (
        'quantity',
        'get_activity'
    )

    list_display = (
        'lineitem_total',
        'order',
        'get_timeslot_summary',
        'get_item_price',
        'updated_quantity',
        'lineitem_total'
    )

    def get_item_price(self, obj):
        if obj.timeslot and obj.timeslot.activity:
            return obj.timeslot.activity.price
        else:
            return None

    get_item_price.short_description = 'Price'

    def get_timeslot_summary(self, obj):
        return f"{obj.timeslot} @ {obj.timeslot.start_time}"

    get_timeslot_summary.short_description = 'Activity'

    def get_activity(self, obj):
        if obj.timeslot and obj.timeslot.activity:
            return obj.timeslot.activity.name
        else:
            return None

    get_activity.short_description = 'Activity'


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, )

    readonly_fields = (
        'order_total',
        'get_id',
        'order_number',
        'date', 'original_basket', 'stripe_pid',
    )

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',
              'original_basket', 'stripe_pid')

    list_display = (
        'user_profile',
        'full_name',
        'get_id',
        'order_number',
        'date',
        'order_total',
    )

    def get_id(self, obj):
        return f'#{obj.id}'

    get_id.short_description = 'Order'

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
