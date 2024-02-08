from django import forms
from betterforms.multiform import MultiModelForm
from .models import Income, Expense
from django import forms


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = (
            "user",
            "start_date",
            "end_date",
            "category",
            "amount",
        )
        widgets = {
            'start_date': forms.DateInput(attrs={"type": "date"}),
            'end_date': forms.DateInput(attrs={"type": "date"})
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = (
            "user",
            "start_date",
            "end_date",
            "category",
            "amount",
        )
        widgets = {
            'start_date': forms.DateInput(attrs={"type": "date"}),
            'end_date': forms.DateInput(attrs={"type": "date"}),
        }


class IN_EX_MultiForm(MultiModelForm):


    form_classes = {
        "Income": IncomeForm,
        "Expense": ExpenseForm,
    }