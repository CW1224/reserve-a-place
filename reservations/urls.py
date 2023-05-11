from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('contact/', views.ContactPage.as_view(), name='contacts'),
    path('menu/', views.MenuPage.as_view(), name='menu'),
    path('booking/', views.BookingPage.as_view(), name='booking'),
    path('reservations/', views.BookingList.as_view(), name='reservations'),
    path('add_booking/', views.AddBooking.as_view(), name='add_booking'),
    path('edit_booking/<str:booking_id>/', views.EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<str:booking_id>/', views.DeleteBooking.as_view(), name='delete_booking'),
]