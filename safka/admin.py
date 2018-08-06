from django.contrib import admin

from safka.models import User, Location, Genre, Product, LocationProduct


@admin.register(LocationProduct)
class LocationProductAdmin(admin.ModelAdmin):
    raw_id_fields = ("location", "product")


admin.site.register(User)
admin.site.register(Location)
admin.site.register(Genre)
admin.site.register(Product)
