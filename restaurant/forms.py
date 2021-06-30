from django import forms
from .models import Reserve


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = '__all__'