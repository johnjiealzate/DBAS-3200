from django.contrib import admin
from .models import Agency, Route,Trip, Stop, StopTime

# Register your models here.
admin.site.register(Agency)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(Stop)
admin.site.register(StopTime)

