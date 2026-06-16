from django import forms
from .models import Task

class Task_Form(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','project','assigned_to',
                'status','priority','due_date']
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'})
        }