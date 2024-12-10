from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .forms import TripForm, StopForm, StopTimeForm
from .models import Trip, Stop, StopTime

# View to create a new trip along with its associated stops and stop times
def create_trip(request):
    if request.method == 'POST':
        trip_form = TripForm(request.POST)
        stop_form = StopForm(request.POST)
        stop_time_form = StopTimeForm(request.POST)
        
        if trip_form.is_valid() and stop_form.is_valid() and stop_time_form.is_valid():
            trip = trip_form.save()
            stop = stop_form.save()
            stop_time = stop_time_form.save(commit=False)
            stop_time.trip = trip
            stop_time.stop = stop
            stop_time.save()
            return redirect('trip_list')

    else:
        # Handle GET request - empty forms for the user to fill out
        trip_form = TripForm()
        stop_form = StopForm()
        stop_time_form = StopTimeForm()

    return render(request, 'rideshare/create_trip.html', {
        'trip_form': trip_form,
        'stop_form': stop_form,
        'stop_time_form': stop_time_form
    })

# Implement a view to display a list of all trips, including related stop names and times.
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'rideshare/trip_list.html', {'trips': trips})


# Implement a view to update an existing trip. Ensure related stops and stop times can also be updated.
def update_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    stop = trip.stop_time_set.first().stop
    stop_time = trip.stop_time_set.first()

    if request.method == 'POST':
        trip_form = TripForm(request.POST, instance=trip)
        stop_form = StopForm(request.POST, instance=stop)
        stop_time_form = StopTimeForm(request.POST, instance=stop_time)

        if trip_form.is_valid() and stop_form.is_valid() and stop_time_form.is_valid():
            trip_form.save()
            stop_form.save()
            stop_time_form.save()

            return redirect('trip_list')
    else:
        trip_form = TripForm(instance=trip)
        stop_form = StopForm(instance=stop)
        stop_time_form = StopTimeForm(instance=stop_time)

    return render(request, 'rideshare/update_trip.html', {
        'trip_form': trip_form,
        'stop_form': stop_form,
        'stop_time_form': stop_time_form
    })

# Implement a view to delete a trip and cascade delete its related `Stops` and `StopTimes`.
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    trip.delete()

    return redirect('trip_list')

def trip_detail(request, id):
    trip = Trip.objects.get(id=id)
    return render(request, 'trip_detail.html', {'trip': trip})
