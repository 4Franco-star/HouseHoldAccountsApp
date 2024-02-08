from typing import Any
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import get_object_or_404
from .forms import IN_EX_MultiForm, IncomeForm, ExpenseForm

from .models import CustomUser, Income, Expense


class Post_Income_AllView(LoginRequiredMixin, ListView):
    model = Income
    template_name = "post/Income_all.html"
    context_object_name = "incomes"
    paginate_by = 2

    def get_queryset(self):
        return Income.objects.select_related("user").filter(user=self.request.user).all()


class Post_Expense_AllView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "post/Expense_all.html"
    context_object_name = "expenses"
    paginate_by = 2

    def get_queryset(self):
        return Expense.objects.select_related("user").filter(user=self.request.user).all()


class InExRegisterView(LoginRequiredMixin, CreateView):
    template_name = "post/create.html"
    form_class = IN_EX_MultiForm
    success_url = reverse_lazy("post:Income_all")


class Income_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    template_name = "post/Income_delete.html"
    success_url = reverse_lazy("post:Income_all")

    def test_func(self):
        income = self.get_object()
        return income.user == self.request.user


class Expense_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Expense
    template_name = "post/Expense_delete.html"
    success_url = reverse_lazy("post:Expense_all")

    def test_func(self):
        expense = self.get_object()
        return expense.user == self.request.user


class Income_UpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "post/Income_update.html"
    success_url = reverse_lazy("post:Income_all")


class Expense_UpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "post/Expense_update.html"
    success_url = reverse_lazy("post:Expense_all")
