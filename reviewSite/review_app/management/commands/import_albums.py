import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from review_app.models import Album, Edition

class Command(BaseCommand):
    help = (
        'Imports albums from a CSV file with the columns',
        'title,artist,release_date,cover_art',
        'the record,boygenius,2023-03-31,cover_art/the_record_boygenius.jpg'
    )

    # require argument
    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')
        parser.add_argument('edition', type=int, help='The Edition to which the albums belong')

    # Call the processing function with the added argument
    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        edition = kwargs.get('edition')
        self.import_albums_from_csv(csv_file_path, edition)

        

    # Process the csv file and write them to album objects.
    def import_albums_from_csv(self, csv_file_path, edition):
        created_a = 0

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists
            for row in reader:
                title, artist, release_date_str, cover_url = row
                release_date = datetime.strptime(release_date_str, '%Y-%M-%d').date()
                
                album, album_created = Album.objects.get_or_create(
                    title=title,
                    artist=artist,
                    release_date=release_date,
                    cover_image=cover_url
                )

                if album_created:
                    created_a += 1
                    Edition.objects.create(year=edition, album_id=album.id)

                
        self.stdout.write(self.style.SUCCESS(f'Successfully imported albums from CSV, added {created_a} new albums.'))