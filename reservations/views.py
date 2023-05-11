from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Booking

class MainPage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "pressed",
            }
        )

class MenuPage(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "menu.html",
            {
                "menu_active": "pressed",
            },
        )

class ContactPage(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            {
                "contact_active": "pressed",
            },
        )

class BookingPage(TemplateView):
    template_name = "booking.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "booking.html",
            {
                "booking_active": "pressed",
            }
        )

class AddBooking(View):
    template_name = 'add_booking.html'

    def get(self, request, *args, **kwargs):
            return render(
                request,
                "add_booking.html",
            )

    def post(self, request):
        fullname = request.POST.get("full_name")
        date = request.POST.get("date")
        time = request.POST.get("time")
        guest_count = request.POST.get("guest_count")
        highchair = request.POST.get("highchair")

        online_booking = Booking.objects.create(
            booking_date=date,
            booking_time=time,
            number_guests=guest_count,
            user=request.user,
        )

        online_booking.save()

        return redirect('reservations')

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-created_date')
    template_name = 'reservations.html'
    paginate_by = 6
    extra_context = {
        "view_booking_active": "pressed"
    }

    def get_queryset(self):
        return Booking.objects.filter(user_id=self.request.user)
    

