from django.db import models
from ulid2 import generate_ulid_as_uuid


class ULIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(default=generate_ulid_as_uuid, primary_key=True)

    class Meta:
        abstract = True


class TimesMixin(models.Model):
    ctime = models.DateTimeField(verbose_name='creation time', editable=False, auto_now_add=True)
    mtime = models.DateTimeField(verbose_name='last modification time', editable=False, auto_now=True)

    class Meta:
        abstract = True
