from django.db.models import Manager
from marshmallow.fields import Nested, missing_


class M2M(Nested):
    def __init__(self, nested, **kwargs):
        kwargs.setdefault("many", True)
        super().__init__(nested, **kwargs)

    def get_value(self, attr, obj, accessor=None, default=missing_):
        try:
            value = getattr(obj, attr)  # Attempt to get the value without calling it
        except AttributeError:
            value = super().get_value(attr, obj, accessor, default)
        if isinstance(value, Manager):
            return value.all()
        return value
