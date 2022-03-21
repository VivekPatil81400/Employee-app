from django import forms
from .models import EmployeeDetail

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ['education', 'department', 'salary', 'manager']