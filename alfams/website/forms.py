from django import forms

from website.models import Pages

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PagesAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', empty_value='<br>', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Pages
        fields = '__all__'
