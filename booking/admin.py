from django.contrib import admin
from .models import CustomUser, Train , Booking
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Train)
admin.site.register(Booking)
