from django.contrib import admin
from django.utils.html import format_html
from .models import Hotel, Image, Location, Amenity


class ImageAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'image']
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Number of empty image forms to display for adding new images
    readonly_fields = ['image_preview']
    fields = ['image', 'image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />'.format(obj.image.url))
        return ""

    image_preview.short_description = 'Preview'

class HotelAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'property_id']
    search_fields = ['title', 'description', 'amenities__name']
    list_filter = ['amenities']

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Location)
admin.site.register(Amenity)