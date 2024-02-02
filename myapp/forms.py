from django import forms
from .models import login

CHOICES = (
    ('1','Male'),
    ('2','Female')
)

class displayform(forms.ModelForm):
    gender = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = login
        fields = '__all__'