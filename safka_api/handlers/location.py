from safka.models import Location
from safka_api.schemata.location import LocationSchema
from safka_api.schemata.product import ProductSchema


def get_locations(request):
    return LocationSchema(many=True).dump(Location.objects.all()).data


def get_location_products(request, id):
    location = Location.objects.get(id=id)
    return ProductSchema(many=True).dump(location.products.all()).data
