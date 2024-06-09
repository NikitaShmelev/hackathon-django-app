# myapp/management/commands/load_data.py

import pandas as pd
from django.core.management.base import BaseCommand
from home.models import Agency, Calendar, CalendarDates, FeedInfo, Routes, Shapes, StopTimes, Stops, Transfers, Trips

class Command(BaseCommand):
    help = 'Load data from provided files into the database'

    def handle(self, *args, **kwargs):
        self.load_agency()
        self.load_calendar()
        self.load_calendar_dates()
        self.load_feed_info()
        self.load_routes()
        self.load_shapes()
        self.load_stops()
        self.load_stop_times()
        self.load_transfers()
        self.load_trips()
        self.stdout.write(self.style.SUCCESS('Successfully loaded all data'))

    def load_agency(self):
        df = pd.read_csv('data/GTFS/agency.txt')
        for _, row in df.iterrows():
            Agency.objects.update_or_create(
                agency_id=row['agency_id'],
                defaults={
                    'agency_name': row['agency_name'],
                    'agency_url': row['agency_url'],
                    'agency_timezone': row['agency_timezone'],
                    'agency_lang': row['agency_lang'],
                    'agency_phone': row['agency_phone'],
                    'agency_fare_url': row['agency_fare_url'],
                    'agency_email': row['agency_email']
                }
            )

    def load_calendar(self):
        df = pd.read_csv('data/GTFS/calendar.txt')
        for _, row in df.iterrows():
            Calendar.objects.update_or_create(
                service_id=row['service_id'],
                defaults={
                    'monday': row['monday'],
                    'tuesday': row['tuesday'],
                    'wednesday': row['wednesday'],
                    'thursday': row['thursday'],
                    'friday': row['friday'],
                    'saturday': row['saturday'],
                    'sunday': row['sunday'],
                    'start_date': row['start_date'],
                    'end_date': row['end_date']
                }
            )

    def load_calendar_dates(self):
        df = pd.read_csv('data/GTFS/calendar_dates.txt')
        for _, row in df.iterrows():
            CalendarDates.objects.update_or_create(
                service_id=row['service_id'],
                defaults={
                    'date': row['date'],
                    'exception_type': row['exception_type']
                }
            )

    def load_feed_info(self):
        df = pd.read_csv('data/GTFS/feed_info.txt')
        for _, row in df.iterrows():
            FeedInfo.objects.update_or_create(
                feed_publisher_name=row['feed_publisher_name'],
                defaults={
                    'feed_publisher_url': row['feed_publisher_url'],
                    'feed_lang': row['feed_lang'],
                    'feed_start_date': row['feed_start_date'],
                    'feed_end_date': row['feed_end_date']
                }
            )

    def load_routes(self):
        df = pd.read_csv('data/GTFS/routes.txt')
        for _, row in df.iterrows():
            Routes.objects.update_or_create(
                route_id=row['route_id'],
                defaults={
                    'agency_id': Agency.objects.get(agency_id=row['agency_id']) if not pd.isna(row['agency_id']) else None,
                    'route_short_name': row['route_short_name'],
                    'route_long_name': row['route_long_name'],
                    'route_desc': row['route_desc'],
                    'route_type': row['route_type'],
                    'route_url': row['route_url'],
                    'route_color': row['route_color'],
                    'route_text_color': row['route_text_color']
                }
            )

    def load_shapes(self):
        df = pd.read_csv('data/GTFS/shapes.txt')
        for _, row in df.iterrows():
            Shapes.objects.update_or_create(
                shape_id=row['shape_id'],
                defaults={
                    'shape_pt_lat': row['shape_pt_lat'],
                    'shape_pt_lon': row['shape_pt_lon'],
                    'shape_pt_sequence': row['shape_pt_sequence'],
                    'shape_dist_traveled': row['shape_dist_traveled']
                }
            )

    def load_stop_times(self):
df = pd.read_csv('data/GTFS/stop_times.txt')
for _, row in df.iterrows():
    StopTimes.objects.update_or_create(
        trip_id=Trips.objects.get(trip_id=row['trip_id']),
        stop_id=Stops.objects.get(stop_id=row['stop_id']),
        defaults={
            'arrival_time': row['arrival_time'],
            'departure_time': row['departure_time'],
            'stop_sequence': row['stop_sequence'],
            'stop_headsign': row['stop_headsign'],
            'pickup_type': row['pickup_type'],
            'drop_off_type': row['drop_off_type'],
            'shape_dist_traveled': row['shape_dist_traveled']
        }
    )

    def load_stops(self):
        df = pd.read_csv('data/GTFS/stops.txt')
        for _, row in df.iterrows():
            Stops.objects.update_or_create(
                stop_id=row['stop_id'],
                defaults={
                    'stop_code': row['stop_code'],
                    'stop_name': row['stop_name'],
                    'stop_desc': row['stop_desc'],
                    'stop_lat': row['stop_lat'],
                    'stop_lon': row['stop_lon'],
                    'stop_url': row['stop_url'],
                    'location_type': row['location_type'],
                    'parent_station': row['parent_station']
                }
            )

    def load_transfers(self):
        df = pd.read_csv('data/GTFS/transfers.txt')
        for _, row in df.iterrows():
            Transfers.objects.update_or_create(
                from_stop_id=row['from_stop_id'],
                to_stop_id=row['to_stop_id'],
                defaults={
                    'transfer_type': row['transfer_type'],
                    'min_transfer_time': row['min_transfer_time']
                }
            )

    def load_trips(self):
        df = pd.read_csv('data/GTFS/trips.txt')
        for _, row in df.iterrows():
            Trips.objects.update_or_create(
                trip_id=row['trip_id'],
                defaults={
                    'route_id': Routes.objects.get(route_id=row['route_id']),
                    'service_id': row['service_id'],
                    'trip_headsign': row['trip_headsign'],
                    'trip_short_name': row['trip_short_name'],
                    'direction_id': row['direction_id'],
                    'block_id': row['block_id'],
                    'shape_id': Shapes.objects.get(shape_id=row['shape_id']) if not pd.isna(row['shape_id']) else None,
                    'wheelchair_accessible': row['wheelchair_accessible']
                }
            )
