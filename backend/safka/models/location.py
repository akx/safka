from django.db import models

from safka.model_mixins import TimesMixin, ULIDPrimaryKeyMixin


class Location(ULIDPrimaryKeyMixin, TimesMixin, models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    frozen_goods = models.TextField(blank=True)
    fresh_goods = models.TextField(blank=True)
    halal_goods = models.TextField(blank=True)
    genres = models.ManyToManyField("safka.Genre")
    products = models.ManyToManyField("safka.Product", through="safka.LocationProduct")

    def __str__(self):
        return f"{self.name}, {self.city}"

    @property
    def n_products(self):
        return self.products.count()
