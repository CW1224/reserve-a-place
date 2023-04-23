from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.BookingList.as_view(), name='reservations.urls'),
]