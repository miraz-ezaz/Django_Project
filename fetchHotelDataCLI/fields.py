from django.db import models

class ImageListField(models.JSONField):
    description = "Stores a list of image paths"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return []
        return list(value)  # Ensure the value is returned as a list

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        return list(value)  # Ensure the value is returned as a list

    def get_prep_value(self, value):
        if not isinstance(value, list):
            raise ValueError('This field requires a list.')
        return super().get_prep_value(value)  # Ensure it's properly serialized as JSON for the database
