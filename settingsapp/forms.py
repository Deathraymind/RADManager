from django import forms
from .models import AppSettings

class AppSettingsForm(forms.ModelForm):
    class Meta:
        model = AppSettings
        fields = '__all__'
