from django import forms
from .models import Trip, Stop, StopTime

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'start_date', 'end_date']

class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = ['location', 'arrival_time', 'departure_time']

class StopTimeForm(forms.ModelForm):
    class Meta:
        model = StopTime
        fields = ['stop', 'trip', 'arrival_time', 'departure_time']
