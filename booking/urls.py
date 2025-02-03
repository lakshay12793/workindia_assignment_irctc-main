
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('add_train/', views.add_train, name='add_train'),
    path('check_availability/<str:source>/<str:destination>/', views.check_availability, name='check_availability'),
    path('book_seat/', views.book_seat, name='book_seat'),
    path('booking_details/', views.get_booking_details, name='get_booking_details'),
]
