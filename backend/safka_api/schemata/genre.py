import marshmallow

from safka.models import Genre


class GenreSchema(marshmallow.Schema):
    class Meta:
        fields = [f.name for f in Genre._meta.fields if not f.many_to_many]
