from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern
    path('api/send_message/', views.send_message, name='send_message'),
    path('api/get_messages/', views.get_messages, name='get_messages'),
    # Add more URL patterns as needed
]