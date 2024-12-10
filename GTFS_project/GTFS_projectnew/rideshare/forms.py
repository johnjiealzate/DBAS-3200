from django import forms
from .models import Trip, Stop, StopTime

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['trip_id', 'route', 'name']
        
class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = ['stop_id', 'stop_name', 'location']

class StopTimeForm(forms.ModelForm):
    class Meta:
        model = StopTime
        fields = ['trip', 'stop', 'arrival_time', 'departure_time']
