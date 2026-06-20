from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description','members', 'status']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
             'members': forms.SelectMultiple(attrs={
                    'class': 'form-control'}
             ),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }