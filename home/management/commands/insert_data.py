import os
from django.core.management.base import BaseCommand
from home.gtfs_parser import ParserGTFS

class Command(BaseCommand):
    help = 'Insert GTFS data from a zip file'

    def add_arguments(self, parser):
        parser.add_argument('zip_file_path', type=str, help='Path to the GTFS zip file')

    def handle(self, *args, **kwargs):
        zip_file_path = kwargs['zip_file_path']

        if not os.path.exists(zip_file_path):
            self.stdout.write(self.style.ERROR('File does not exist: {}'.format(zip_file_path)))
            return

        parser = ParserGTFS(zip_file_path)
        parser.parse()

        self.stdout.write(self.style.SUCCESS('GTFS data inserted successfully.'))
