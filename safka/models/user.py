from django.contrib.auth.models import AbstractUser

from safka.model_mixins import ULIDPrimaryKeyMixin


class User(ULIDPrimaryKeyMixin, AbstractUser):
    pass
