from .models import Booking
from django import forms
from django.forms import ModelForm

class UpdateBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'booking_date', 'booking_time', 'number_guests', 'high_chair')
