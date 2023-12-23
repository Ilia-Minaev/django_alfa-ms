from django import forms

from ecommerce.models import Order

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class OrderAdminForm(forms.ModelForm):
    order = forms.CharField(label='Заказ', empty_value='<br>', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Order
        fields = '__all__'
