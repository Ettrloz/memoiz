from django.urls import path

from .views import SignInView, SignOutView

urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("signout/", SignOutView.as_view(), name="signout"),
]
