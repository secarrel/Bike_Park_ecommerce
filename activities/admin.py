from django.contrib import admin
from .models import Category, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
        'activity',
        'review_time'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
