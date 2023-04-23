from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_date')
    actions = ['approve_booking']
    list_display = ['user', 'number_guests', 'high_chair','booking_date', 'booking_time', 'status']
    search_fields = ['user', 'created_date', 'status', 'booking_date']
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)