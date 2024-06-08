from django.db import models
from .base_model import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=50)
    second_title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
