from django import forms
from .models import Reserve


class ReserveTableForm(forms.ModelForm):
    time=forms.TimeField(input_formats=['%H:%M'])
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Reserve
        fields = '__all__'