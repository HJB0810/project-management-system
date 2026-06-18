from django import forms
from .models import Task

class Task_Form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user',None)
        super().__init__(*args,**kwargs)
        if user:
            self.fields['project'].queryset=(
                user.joined_projects.all()  |
                user.created_projects.all()
            ).distinct()
            
    class Meta:
        model=Task
        fields=['title','description','project','assigned_to',
                'status','priority','due_date']
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'})
        }