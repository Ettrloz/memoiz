from django.shortcuts import redirect
from django.views.generic import TemplateView


def homepage(request):
    return redirect("app/")


class AppView(TemplateView):
    template_name = "app.html"
