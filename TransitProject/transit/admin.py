from django.contrib import admin
from .models import Agency, Routes, Trips, Stops, StopTimes

# Register your models here.
admin.site.register(Agency)
admin.site.register(Routes)
admin.site.register(Trips)
admin.site.register(Stops)
admin.site.register(StopTimes)
