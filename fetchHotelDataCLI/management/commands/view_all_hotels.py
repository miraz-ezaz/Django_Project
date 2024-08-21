from django.core.management.base import BaseCommand
from fetchHotelDataCLI.models import Listing


class Command(BaseCommand):
    help = 'Display all hotel details from the scrapdb database'

    def handle(self, *args, **kwargs):
        listings = Listing.objects.using('scrapdb').all()

        if listings.exists():
            self.stdout.write(self.style.SUCCESS('List of Hotels:'))
            for listing in listings:
                self.stdout.write(
                    f"Title: {listing.title}, Address: {listing.location}, Rating: {listing.rating}")
        else:
            self.stdout.write(self.style.WARNING(
                'No Hotels found in the database.'))
