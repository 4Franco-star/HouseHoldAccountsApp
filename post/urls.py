from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("Income/all/", views.Post_Income_AllView.as_view(), name="Income_all"),
    path("Expense/all/", views.Post_Expense_AllView.as_view(), name="Expense_all"),
    path("create/", views.InExRegisterView.as_view(), name="create"),
    path("Income/<int:pk>/delete/", views.Income_DeleteView.as_view(), name="Income_delete"),
    path("Expense/<int:pk>/delete/", views.Expense_DeleteView.as_view(), name="Expense_delete"),
    path("Income/<int:pk>/update/", views.Income_UpdateView.as_view(), name="Income_update"),
    path("Expense/<int:pk>/update/", views.Expense_UpdateView.as_view(), name="Expense_update"),

]
