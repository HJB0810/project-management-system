from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }