from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.homepage, name="index"),
    path("app/", views.AppView.as_view(), name="app"),
    path("memoiz/", include("memoiz.urls", namespace="memoiz")),
]
