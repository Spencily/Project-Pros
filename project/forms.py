from django import forms
from .models import project_detail, emoji

class project_detailForm(forms.ModelForm):
    class Meta:
        model = project_detail
        fields = ['title', 'summary', 'collaborators', 'deployed_site', 'github_repo', 'reflections', 'approved', 'favourite',]
        widgets = {
            'title' : forms.TextInput (attrs= {
                'class' : 'form-control',
                'placeholder': 'enter project name',
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter project summary',
            }),
            'collaborators': forms.Textarea (attrs= {
                'class': 'form-control',
                'placeholder': 'enter name/names'
            }),
            'deployed_site': forms.TextInput (attrs= {
                'class' : 'form-control',
                'placeholder': 'enter deployed link',
            }),
            'github_repo': forms.TextInput (attrs= {
                'class' : 'form-control',
                'placeholder': 'enter repo link',
            }),
            'reflections': forms.Textarea (attrs= {
                'class': 'form-control',
            }),
            'approved': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'favourite': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

class EmojiSelection(forms.ModelForm):
    class Meta:
        model = emoji
        fields = ['fontawesome_classname',]