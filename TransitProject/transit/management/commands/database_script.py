from django.core.management.base import BaseCommand
from transit.models import Agency, Routes, Trips, Stops, StopTimes
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample Agencies
        agency = Agency.objects.create(
            agency_id='agency1',
            name='Sample Transit Agency',
        )

        # Create sample Routes
        route1 = Routes.objects.create(
            route_id='route1',
            agency=agency,
            long_name='Main Street Line',
        )

        route2 = Routes.objects.create(
            route_id='route2',
            agency=agency,
            long_name='Broadway Line',
         )

        # Create sample Stops
        stop1 = Stops.objects.create(
            stop_id='stop1',
            stop_name='Main Street Station',
            stop_lat=40.7128,
            stop_lon=-74.0060
        )

        stop2 = Stops.objects.create(
            stop_id='stop2',
            stop_name='Broadway Junction',
            stop_lat=40.7150,
            stop_lon=-74.0100
        )

        # Create sample Trips
        trip1 = Trips.objects.create(
            trip_id='trip1',
            route=route1,
        )

        trip2 = Trips.objects.create(
            trip_id='trip2',
            route=route2,
        )

        # Create sample StopTimes
        StopTimes.objects.create(
            trip=trip1,
            stop=stop1,
            arrival_time=datetime.now().time(),
            departure_time=(datetime.now() + timedelta(minutes=5)).time(),
            stop_sequence=1
        )

        StopTimes.objects.create(
            trip=trip2,
            stop=stop2,
            arrival_time=(datetime.now() + timedelta(minutes=10)).time(),
            departure_time=(datetime.now() + timedelta(minutes=15)).time(),
            stop_sequence=1
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
