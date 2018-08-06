import marshmallow

from safka.models import Product


class ProductSchema(marshmallow.Schema):
    class Meta:
        fields = [f.name for f in Product._meta.local_concrete_fields]
