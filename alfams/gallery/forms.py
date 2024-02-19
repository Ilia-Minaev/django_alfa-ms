from typing import Any
from django import forms
from gallery.models import Name, Images
from django.core.files.uploadedfile import SimpleUploadedFile

class GalltryForm(forms.ModelForm):
    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)

    class Meta:
        model = Images
        fields = ('parent', 'image')
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-select', 'size': "10"}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'multiple': '' }),
        }