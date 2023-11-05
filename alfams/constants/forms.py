from django import forms

class PhoneAdminForm(forms.ModelForm):
    phone1 = forms.CharField()
    phone2 = forms.CharField()