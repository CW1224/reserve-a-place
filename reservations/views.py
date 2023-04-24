from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Booking

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6
