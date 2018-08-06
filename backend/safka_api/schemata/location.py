import marshmallow
from marshmallow import fields

from safka.models import Location
from safka_api.fields import M2M
from safka_api.schemata.genre import GenreSchema


class LocationSchema(marshmallow.Schema):
    genres = M2M(GenreSchema(many=True))
    n_products = fields.Int(read_only=True)

    class Meta:
        fields = [f.name for f in Location._meta.fields] + ["genres", "n_products"]
