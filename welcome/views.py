from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class WelcomeView(TemplateView):
    template_name = "welcome/welcome.html"
