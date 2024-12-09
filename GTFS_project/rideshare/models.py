from django.db import models

# Model for Trip
class Trip(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

# Model for Stop
class Stop(models.Model):
    location = models.CharField(max_length=200)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    def __str__(self):
        return self.location

# Model for StopTime
class StopTime(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"Stop: {self.stop.location} for Trip: {self.trip.name}"
