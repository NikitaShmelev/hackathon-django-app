import os
import zipfile
from models import *

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
        
    def process_file_line_by_line(func):
        def wrapper(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    func(line)
        return wrapper
    
    def prarse(self):
        for file in self.get_all_files().items():
            if file[1].contains('routes'):
                self.parse_routes(file)
            elif file[1].contains('trips'):
                self.parse_trips(file)
            elif file[1].contains('calendar'):
                self.parse_calendar(file)
            elif file[1].contains('calendar_dates'):
                self.parse_calendar_dates(file)
            elif file[1].contains('transfers'):
                self.parse_transfers(file)
            elif file[1].contains('feed_info'):
                self.parse_feed_info(file)
            elif file[1].contains('agency'):
                self.parse_agency(file)
            elif file[1].contains('shapes'):
                self[1].parse_shapes(file)
            elif file[1].contains('stop_times'):
                self.parse_stop_times(file)
            elif file[1].contains('stops'):
                self.parse_stops(file)
    
    @process_file_line_by_line
    def parse_feed_info(self,line):
        data = line.split(',')
        try:
            FeedInfo.objects.create(
                feed_publisher_name=data[0],
                feed_publisher_url=data[1],
                feed_lang=data[2],
                feed_start_date=data[3],
                feed_end_date=data[4],
            )
        except Exception as e:
            print(e)
    
    @process_file_line_by_line
    def parse_transfers(self, line):
        data = line.split(',')
        try:
            Transfers.objects.create(
                from_stop_id=data[0],
                to_stop_id=data[1],
                transfer_type=data[2],
                min_transfer_time=data[3]
            )
        except Exception as e:
            print(e)
    
    @process_file_line_by_line
    def parse_calendar_dates(self, line):
        data = line.split(',')
        try:
            CalendarDates.objects.create(
                service_id=data[0],
                date=data[1],
                exception_type=data[2]
            )
        except Exception as e:
            print(e)
    
    @process_file_line_by_line
    def parse_agency(self, line):
        data = line.split(',')
        try:
            Agency.objects.create(
                agency_id=data[0],
                agency_name=data[1],
                agency_url=data[2],
                agency_timezone=data[3],
                agency_lang=data[4],
                agency_phone=data[5],
                agency_fare_url=data[6]
            )
        except Exception as e:
            print(e)
            
    @process_file_line_by_line
    def parse_stops(self, line):
        data = line.split(',')
        try:
            Stops.objects.create(
                stop_id=data[0],
                stop_code=data[1],
                stop_name=data[2],
                stop_desc=data[3],
                stop_lat=data[4],
                stop_lon=data[5],
                stop_url=data[6],
                location_type=data[7],
                parent_station=data[8]
            )
        except Exception as e:
            print(e)
            
    @process_file_line_by_line
    def prse_calendar(self, line):
        data = line.split(',')
        try:
            Calendar.objects.create(
                route_id=data[0],
                service_id=data[1],
                trip_id=data[2],
                trip_headsign=data[3],
                trip_short_name=data[4],
                direction_id=data[5],
                block_id=data[6],
                shape_id=data[7],
                wheelchari_accessible=data[8],
            )
        except Exception as e:
            print(e)
            
    @process_file_line_by_line    
    def parse_trips(self, line):
        data = line.split(',')
        try:
            Trips.objects.create(
                route_id=data[0],
                service_id=data[1],
                trip_id=data[2],
                trip_headsign=data[3],
                trip_short_name=data[4],
                direction_id=data[5],
                block_id=data[6],
                shape_id=data[7],
                wheelchair_accessible=data[8]
            )
        except Exception as e:
            print(e)
    
    @process_file_line_by_line    
    def parse_routes(self, line):
        data = line.split(',')
        try:
            Routes.objects.create(
                route_id=data[0],
                agency_id=data[1],
                route_short_name=data[2],
                route_long_name=data[3],
                route_desc=data[4],
                route_type=data[5],
                route_url=data[6],
                route_color=data[7],
                route_text_color=data[8]
            )
        except Exception as e:
            print(e)
            
    @process_file_line_by_line
    def parse_shapes(self, line):
        data = line.split(',')
        try:
            Shapes.objects.create(
                shape_id=data[0],
                shape_pt_lat=data[1],
                shape_pt_lon=data[2],
                shape_pt_sequence=data[3],
                shape_dist_traveled=data[4]
            )
        except Exception as e:
            print(e)
    
    @process_file_line_by_line
    def parse_stop_times(self, line):
        data = line.split(',')
        try:
            StopTimes.objects.create(
                trip_id=data[0],
                arrival_time=data[1],
                departure_time=data[2],
                stop_id=data[3],
                stop_sequence=data[4],
                stop_headsign=data[5],
                pickup_type=data[6],
                drop_off_type=data[7],
                shape_dist_traveled=data[8]
            )
        except Exception as e:
            print(e)
                    
    def get_all_files(self):
        files = self.get_files_from_zip() if self.file_path.contains('.zip') else [self.file_path] 
        file_path = {}
        for file in self.GTFS_FILES:
            file_path[file] = [ f for f in files if f.contains(file)]
        
        
    def get_files_from_zip(self):
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            zip_ref.extractall('tmp')
        return list(map(lambda x: (f"tmp/{x}"), os.listdir('tmp')))