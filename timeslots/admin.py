from django.contrib import admin
from .models import Timeslot
from activities.models import Activity


class TimeslotInline(admin.TabularInline):
    model = Timeslot

    readonly_fields = (
        'spaces_booked',
        'format_date',
        'format_starttime',
        'get_endtime',
        'get_duration',
    )

    list_display = (
        'title',
        'activity',
        'available_capacity',
    )

    def title(self, obj):
        return f"{obj.activity} - {obj.start_time.strftime(
            '%d/%m/%Y @ %H:%M')}"

    title.short_description = 'Item'

    def format_date(self, obj):
        return obj.start_time.strftime('%A, %d %B %Y')

    format_date.short_description = 'Date'

    def format_starttime(self, obj):
        return obj.start_time.strftime('%H:%M')

    format_starttime.short_description = 'Current Start Time'

    def get_endtime(self, obj):
        if obj.start_time and obj.activity and obj.activity.duration:
            end_time = obj.start_time + obj.activity.duration
            return end_time.strftime('%H:%M')
        else:
            return None

    get_endtime.short_description = 'End Time'

    def get_duration(self, obj):
        if obj.activity and obj.activity.duration:
            duration = obj.activity.duration
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            if minutes == 0:
                return f"{hours} hrs"
            else:
                return f"{hours} hrs {minutes} mins"
        else:
            return None

    get_duration.short_description = 'Duration'


class ActivityAdmin(admin.ModelAdmin):
    inlines = [TimeslotInline]
    list_display = (
        'name',
        'category_name',
        'difficulty',
        'capacity',
        'price',
        'get_duration',
    )

    ordering = ('category',)

    def category_name(self, obj):
        return obj.category.friendly_name

    category_name.short_description = 'Catgeory'

    def get_duration(self, obj):
        if obj.duration:
            duration = obj.duration
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            if minutes == 0:
                return f"{hours} hrs"
            else:
                return f"{hours} hrs {minutes} mins"
        else:
            return None

    get_duration.short_description = 'Duration'


admin.site.register(Activity, ActivityAdmin)
