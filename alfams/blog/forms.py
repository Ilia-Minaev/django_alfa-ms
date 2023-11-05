from django import forms

from blog.models import Articles, Portfolio

from ckeditor_uploader.widgets import CKEditorUploadingWidget



class ArticlesAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', empty_value='<br>', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Articles
        fields = '__all__'

class PortfolioAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', empty_value='<br>', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Portfolio
        fields = '__all__'