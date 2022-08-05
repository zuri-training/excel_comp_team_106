from socket import fromshare
from django import forms
from .models import File

class FileForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = File
        fields = ('title', 'file')

