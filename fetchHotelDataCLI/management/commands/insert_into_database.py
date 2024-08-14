import os
import shutil
from django.core.management.base import BaseCommand
from fetchHotelDataCLI.models import Listing
from hotels.models import Hotel, Image
from django.conf import settings
from django.db import transaction
import uuid

def hotel_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    unique_id = uuid.uuid4().hex[:8]
    filename = f"{instance.hotel.property_id}_{instance.hotel.title}_{unique_id}.{ext}"
    return os.path.join('images', filename)

class Command(BaseCommand):
    help = 'Import hotels from scrapdb to the default database and move images to media folder'

    def handle(self, *args, **kwargs):
        listings = Listing.objects.using('scrapdb').all()

        if not listings.exists():
            self.stdout.write(self.style.WARNING('No listings found in the scrapdb database.'))
            return

        for listing in listings:
            with transaction.atomic():
                # Check if a hotel with the same title already exists
                existing_hotel = Hotel.objects.filter(title=listing.title).first()

                if existing_hotel:
                    self.stdout.write(self.style.WARNING(f"Hotel with title '{listing.title}' already exists. Skipping..."))
                    continue

                # Create a new hotel in the default database
                hotel = Hotel.objects.create(
                    title=listing.title,
                    description=f'Imported from scrapdb: {listing.title}',
                )
                self.stdout.write(self.style.SUCCESS(f'Created Hotel: {hotel.title}'))

                if isinstance(listing.images, list):
                    for image_path in listing.images:
                        self.save_image(hotel, image_path)
                else:
                    self.stdout.write(self.style.WARNING(f'No images found or invalid format for {hotel.title}.'))

    def save_image(self, hotel, image_path):
        scrapy_image_dir = settings.SCRAPY_IMAGE_DIR
        full_image_path = os.path.join(scrapy_image_dir, image_path.replace(" ","_"))
        try:
            if not os.path.isfile(full_image_path):
                self.stderr.write(self.style.ERROR(f'Image not found: {full_image_path}'))
                return

            original_filename = os.path.basename(full_image_path)
            image_instance = Image(hotel=hotel)
            new_filename = hotel_image_file_path(image_instance, original_filename)

            dest_path = os.path.join(settings.MEDIA_ROOT, new_filename)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            shutil.copy(full_image_path, dest_path)

            image_record = Image.objects.create(hotel=hotel, image=new_filename)
            self.stdout.write(self.style.SUCCESS(f'Added Image: {image_record.image.url} for Hotel: {hotel.title}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Failed to copy {full_image_path}: {e}'))
