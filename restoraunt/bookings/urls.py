from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('bookings/add-bookings/', add_bookings , name = 'add-bookings')

]

