from django.core.management.base import BaseCommand
from fetchHotelDataCLI.models import Listing

class Command(BaseCommand):
    help = 'Display all hotel titles from the scrapdb database'

    def handle(self, *args, **kwargs):
        listings = Listing.objects.using('scrapdb').all()

        if listings.exists():
            self.stdout.write(self.style.SUCCESS('Listing Titles:'))
            for listing in listings:
                self.stdout.write(listing.title)
        else:
            self.stdout.write(self.style.WARNING('No listings found in the database.'))
