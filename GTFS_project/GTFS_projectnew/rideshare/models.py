from django.db import models

# Model for Agency
class Agency(models.Model):
    agency_id = models.CharField(max_length=10)
    agency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.agency_name

# Model for Route
class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=100)

    def __str__(self):
        return self.route_name
    
# Model for Trip
class Trip(models.Model):
    trip_id = models.CharField(max_length=10, primary_key=True)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# Model for Stop
class Stop(models.Model):
    stop_id = models.CharField(max_length=100, default="default_stop_id")
    stop_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location

# Model for StopTime
class StopTime(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return f"Stop: {self.stop.location} for Trip: {self.trip.name}"

