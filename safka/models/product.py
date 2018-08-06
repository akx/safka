from django.db import models

from safka.model_mixins import TimesMixin, ULIDPrimaryKeyMixin


class Product(ULIDPrimaryKeyMixin, TimesMixin, models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"
