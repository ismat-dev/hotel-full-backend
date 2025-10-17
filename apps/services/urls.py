from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.ServiceView.as_view()),
    path('services_create/', views.ServiceCreate.as_view()),
    path('services_updatedelete/<int:pk>/', views.ServiceUpdateAndDelete.as_view()),

    path('sevices/', views.ServiceaCreateByMeneger.as_view())
]
