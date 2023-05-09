from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('reservation_detail/<str:booking_id>/', views.BookingDetail.as_view(), name='reservation_detail.urls'), 
    path('', views.BookingList.as_view(), name='reservations.urls'),
]