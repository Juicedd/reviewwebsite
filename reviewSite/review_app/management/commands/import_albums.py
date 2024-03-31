import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from review_app.models import Album

class Command(BaseCommand):
    help = 'Imports albums from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        self.import_albums_from_csv(csv_file_path)

    def import_albums_from_csv(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists
            for row in reader:
                title, artist, release_date_str = row
                release_date = datetime.strptime(release_date_str, ' %d-%m-%Y').date()
                Album.objects.create(title=title, artist=artist, release_date=release_date)
        self.stdout.write(self.style.SUCCESS('Successfully imported albums from CSV'))



def import_albums_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            title, artist, release_date = row
            release_date = datetime.strptime(release_date, '%D-%M-%Y').date()
            Album.objects.create(title=title, artist=artist, release_date=release_date)

if __name__ == '__main__':
    file_path = 'C:\\Users\\nicol\\OneDriveJoost\\OneDrive\\Documenten\\Coding\\reviewwebsite\\reviewSite\\review_app\\migrations\\AOTY_albums2023.csv'
    import_albums_from_csv(file_path)