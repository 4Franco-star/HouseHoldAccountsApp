from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("all/", views.AllView.as_view(), name="all"),
]
