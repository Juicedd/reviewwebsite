import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from review_app.models import Album

class Command(BaseCommand):
    help = 'Imports albums from a CSV file'

    # require argument
    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')


    # Call the processing function with the added argument
    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        self.import_albums_from_csv(csv_file_path)

    # Process the csv file and write them to album objects.
    def import_albums_from_csv(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists
            for row in reader:
                title, artist, release_date_str = row
                release_date = datetime.strptime(release_date_str, '%Y-%M-%d').date()
                Album.objects.create(title=title, artist=artist, release_date=release_date)
        self.stdout.write(self.style.SUCCESS('Successfully imported albums from CSV'))