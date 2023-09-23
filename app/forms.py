from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['NAME', 'UGPA', 'RCN', 'TOEFL', 'LOR', 'SOP', 'HIGH_SCHOOL_POINTS']