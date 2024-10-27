from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_hotspot, name='start_hotspot'),
    path('stop/', views.stop_hotspot, name='stop_hotspot'),
    path('status/', views.show_hotspot_status, name='show_hotspot_status'),
]