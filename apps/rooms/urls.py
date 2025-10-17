from django.urls import path

from . import views

urlpatterns = [
    path('roomslistorcreate/', views.Roomsviews.as_view()),
    path('rommsupdateand_Delete/<int:pk>/', views.RoomsUpdateAndDelete.as_view()),
]
