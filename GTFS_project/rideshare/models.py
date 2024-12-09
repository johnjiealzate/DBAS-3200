from django.db import models

# Create your models here.
class Agency(models.Model):
    agency_id = models.CharField(max_length=50, primary_key=True)
    agency_name = models.CharField(max_length=100, default='Default Agency')

    def __str__(self):
        return self.agency_name


class Routes(models.Model):
    route_id = models.CharField(max_length=50, primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    route_long_name = models.CharField(max_length=100)

    def __str__(self):
        return self.route_long_name


class Trips(models.Model):
    trip_id = models.CharField(max_length=50, primary_key=True)
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_id


class Stops(models.Model):
    stop_id = models.CharField(max_length=50, primary_key=True)
    stop_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stop_name


class StopTimes(models.Model):
    stop_time_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stops, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return f"{self.trip.trip_id} - {self.stop.stop_name}"