from typing import Any
from django import forms
from gallery.models import Name, Images
from django.core.files.uploadedfile import SimpleUploadedFile

class GalltryForm(forms.ModelForm):
    #name = forms.CharField(max_length=150, label='Введите название серии')
    #new_name = forms.ModelChoiceField(label='Выберете существующую название серии', queryset=Name.objects.all())
    #message = forms.CharField(widget=forms.Textarea)

    #def send_email(self):
    #    # send email using the self.cleaned_data dictionary
    #    pass

    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)

    class Meta:
        model = Images
        fields = ('parent', 'image')
        #fields = '__all__'
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-select', 'size': "10"}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'multiple': '' }),
            #'image': forms.FileInput(attrs={'class': 'form-control',}),
            #'image': forms.Imag(attrs={'class': 'form-control',}),
        }