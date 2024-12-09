from django import forms
from .models import Trip, Stop, StopTimes

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
        model = StopTimes
        fields = ['stop', 'trip', 'arrival_time', 'departure_time']
