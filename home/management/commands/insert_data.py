import os
import zipfile
from django.core.management.base import BaseCommand
# from home.gtfs_parser import ParserGTFS
from home.models import *

class ParserGTFS:
    GTFS_FILES = [
    'agency.txt',
    'stops.txt',
    'routes.txt',
    'calendar.txt',
    'calendar_dates.txt',
    'trips.txt',
    'stop_times.txt',
    'transfers.txt',
    'shapes.txt',
    'feed_info.txt'
    ]
    
    def __init__(self, file_path) -> None:
        self.file_path = file_path
    
    def file_reader(self, file_path):
        lines = []
        with open(file_path[1], 'r') as file:
            for line in file:
                lines.append(line)
        return lines[1:] if len(lines) > 1 else []
        
    def parse(self):
        for file in self.get_all_files().items():
            if 'routes' in file[1]:
                self.parse_routes(file)
            elif 'trips' in file[1]:
                self.parse_trips(file)
            elif 'calendar' in file[1] and file[1] != 'calendar_dates':
                self.parse_calendar(file)
            elif 'calendar_dates' in file[1]:
                self.parse_calendar_dates(file)
            elif 'transfers' in file[1]:
                self.parse_transfers(file)
            elif 'feed_info' in file[1]:
                self.parse_feed_info(file)
            elif 'agency' in file[1]:
                self.parse_agency(file)
            elif 'shapes' in file[1]:
                self.parse_shapes(file)
            elif 'stop_times' in file[1]:
                self.parse_stop_times(file)
            elif 'stops' in file[1]:
                self.parse_stops(file)

    def parse_feed_info(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            FeedInfo.objects.create(
                feed_publisher_name=data[0],
                feed_publisher_url=data[1],
                feed_lang=data[2],
                feed_start_date=data[3],
                feed_end_date=data[4],
            )
    
    def parse_transfers(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            Transfers.objects.create(
                from_stop_id=int(data[0]),
                to_stop_id=int(data[1]),
                transfer_type=data[2],
                min_transfer_time=data[3]
            )
    
    def parse_calendar_dates(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            CalendarDates.objects.create(
                service_id=int(data[0]),
                date=data[1],
                exception_type=data[2]
            )
    
    def parse_agency(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            Agency.objects.create(
                agency_id=int(data[0]),
                agency_name=data[1],
                agency_url=data[2],
                agency_timezone=data[3],
                agency_lang=data[4],
                agency_phone=data[5],
                agency_fare_url=data[6]
            )
            
    def parse_stops(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            Stops.objects.create(
                stop_id=int(data[0]),
                stop_code=data[1],
                stop_name=data[2],
                stop_desc=data[3],
                stop_lat=data[4],
                stop_lon=data[5],
                stop_url=data[6],
                location_type=data[7],
                parent_station=data[8]
            )
            
    def parse_calendar(self, file_path):
        pass
    #    for line in self.file_reader(file_path):
    #         data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))

            
    def parse_trips(self, file_path):
       for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            Trips.objects.create(
                route_id=Routes.objects.get_or_create(route_id=int(data[0]))[0],
                service_id=int(data[1]),
                trip_id=int(data[2]),
                trip_headsign=data[3],
                trip_short_name=data[4],
                direction_id=int(data[5]),
                block_id=int(data[6]),
                shape_id= Shapes.objects.get_or_create(shape_id = int(data[7]))[0],
                wheelchair_accessible=data[8]
            )

    def parse_routes(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            Routes.objects.create(
                route_id= int(data[0]),
                agency_id= int(data[1]) if data[1] else None,
                route_short_name=data[2],
                route_long_name=data[3],
                route_desc=data[4],
                route_type=data[5],
                route_url=data[6],
                route_color=data[7],
                route_text_color=data[8]
            )

            
    def parse_shapes(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            Shapes.objects.create(
                shape_id=int(data[0]),
                shape_pt_lat=data[1],
                shape_pt_lon=data[2],
                shape_pt_sequence=data[3],
                shape_dist_traveled=data[4]
            )

    
    def parse_stop_times(self, file_path):
        for line in self.file_reader(file_path):
            data = list(map( lambda x: x if x and x != '\n' else None, [ l for l in  line.split(',')]))
            StopTimes.objects.create(
                trip_id= Trips.objects.get_or_create(trip_id=int(data[0]))[0] ,
                arrival_time=data[1],
                departure_time=data[2],
                stop_id= Stops(int(data[3])),
                stop_sequence=data[4],
                stop_headsign=data[5],
                pickup_type=data[6],
                drop_off_type=data[7],
                shape_dist_traveled=data[8]
            )

                    
    def get_all_files(self):
        files = self.get_files_from_zip() if '.zip' in self.file_path else [self.file_path] 
        file_path = {}
        for file in self.GTFS_FILES:
            file_path[file] = [ f for f in files if file in f][0]
        return file_path
        
    def get_files_from_zip(self):
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            zip_ref.extractall('tmp')
        return list(map(lambda x: (f"tmp/GTFS/{x}"), os.listdir('tmp/GTFS')))

class Command(BaseCommand):
    help = 'Insert GTFS data from a zip file'

    def add_arguments(self, parser):
        parser.add_argument('zip_file_path', type=str, help='Path to the GTFS zip file')

    def handle(self, *args, **kwargs):
        zip_file_path = kwargs['zip_file_path']
        if not os.path.exists(zip_file_path):
            self.stdout.write(self.style.ERROR('File does not exist: {}'.format(zip_file_path)))
            return
        ParserGTFS(zip_file_path).parse()

        self.stdout.write(self.style.SUCCESS('GTFS data inserted successfully.'))
