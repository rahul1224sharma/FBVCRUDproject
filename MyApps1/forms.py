from django import forms
from MyApps1.models import Employee
class EmployeeForm(forms.Form):
    class Meta:
        model=Employee
        fields='__all__'