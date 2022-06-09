from django.urls import path

urlpatterns = [
    path('', index),
    path('detail/<int:pk>', detail)
]