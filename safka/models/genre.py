from django.db import models

from safka.model_mixins import ULIDPrimaryKeyMixin


class Genre(ULIDPrimaryKeyMixin, models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"
