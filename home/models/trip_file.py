from django.db import models
from .base_model import BaseModel

from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if not value.name.endswith(".txt") and not value.name.endswith(".csv"):
        raise ValidationError(
            "Unsupported file extension. Only .txt and .csv files are allowed."
        )


class TripFile(BaseModel):
    file = models.FileField(upload_to="uploads/", validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
