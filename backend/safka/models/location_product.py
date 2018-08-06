from django.conf import settings
from django.db import models

from safka.model_mixins import ULIDPrimaryKeyMixin, TimesMixin


class LocationProduct(ULIDPrimaryKeyMixin, TimesMixin, models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    product = models.ForeignKey("safka.Product", on_delete=models.CASCADE)
    location = models.ForeignKey("safka.Location", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('product', 'location'),)

    def __str__(self):
        return f"{self.product} @ {self.location}"
