from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Booking

class MainPage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
        )

class MenuPage(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "menu.html",
        )

class ContactPage(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
        )

class BookingDetail(View):
    template_name = 'reservation_detail.html'

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(status=1)
        return render(
            request,
            "index.html"
        )


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-created_date')
    template_name = 'reservations.html'
    paginate_by = 6
