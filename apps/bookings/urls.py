from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.UserBookings.as_view()),
    path('bookings_check_reciptionest/', views.Bookings.as_view()),

    path('bookingsupdateordelete/<int:pk>/', views.UserBookingsUpdateOrDelete.as_view()),
    path('roomviews/', views.RoomView.as_view())
]
