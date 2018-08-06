from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("safka_api.urls", namespace="safka_api")),
    path("", include("safka.urls")),
]
