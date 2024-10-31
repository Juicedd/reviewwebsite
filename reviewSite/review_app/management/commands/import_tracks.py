import csv
from django.core.management.base import BaseCommand
from review_app.models import Album, Track
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Imports tracks from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        self.import_tracks_from_csv(csv_file_path)

    def import_tracks_from_csv(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists
            for row in reader:
                album_title, track_title, track_number = row
                try:
                    album = Album.objects.get(title=album_title)
                    Track.objects.create(
                        album=album,
                        title=track_title,
                        track_number=int(track_number)
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Successfully added track: {track_title} to album: {album_title}'
                    ))
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f'Album not found: {album_title}'
                    ))
