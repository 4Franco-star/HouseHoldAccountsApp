from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from accounts.models import CustomUser


class AllView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "post/all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        Logged_in_user = get_object_or_404(CustomUser, username=user)
        context["Logged_in_user"] = Logged_in_user
        return context
