from django import forms
from .models import Task
from django.db.models import Q
from django.contrib.auth.models import User
from projects.models import Project

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

    def __init__(self,*args,user=None,**kwargs):
        super().__init__(*args,**kwargs)

        if user:
            self.fields['project'].queryset = Project.objects.filter(
                Q(created_by=user)|
                Q(members=user)
            ).distinct()

        if self.instance.pk:
            project= self.instance.project
            self.fields['assigned_to'].queryset =(
                project.members.all()|
                User.objects.filter(id=project.created_by.id)
            ).distinct()

    


