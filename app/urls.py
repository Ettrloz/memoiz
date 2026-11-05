from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("django_vite_plugin.urls")),
    path("", include("authentication.urls")),
]
