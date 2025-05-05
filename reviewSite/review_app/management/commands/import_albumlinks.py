import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from review_app.models import Album, AlbumLink

class Command(BaseCommand):
    help = (
        'Imports the urls from a file to the table albumlinks',
        'table format is',
        'album_id, link_type, url'
        '25, spotify, https://www.loremipsum.com'
    )

    # require argument
    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')

    # Call the processing function with the added argument
    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        self.import_urls_from_csv(csv_file_path)

    # Process the csv file and write them to album objects.
    def import_urls_from_csv(self, csv_file_path):
        created_urls = 0

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists
            for row in reader:
                title, link_type, url = row
                try:
                    album = Album.objects.get(title=title)
                    album_id = album.id
                    alink, link_created = AlbumLink.objects.get_or_create(
                        album_id=album_id,
                        link_type=link_type,
                        url = url
                    )
                    if link_created:
                        created_urls += 1
                except Album.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Album with title "{title}" does not exist. Skipping.'))
                    continue
                
        self.stdout.write(self.style.SUCCESS(f'Successfully imported album links from CSV, added {created_urls} new urls.'))