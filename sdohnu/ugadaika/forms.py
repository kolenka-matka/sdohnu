from django import forms
from .models import Artists
from django.forms import ModelForm, TextInput, NumberInput

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class StyleChoice(forms.Form):
    style = forms.BooleanField(label='экшн', required=False)

class ArtistsForm(ModelForm):
    class Meta:
        model = Artists
        fields = ['name', 'biography', 'date_birth', 'date_death', 'image']


        widgets = {
            'name': TextInput(attrs={
                'class': 'sdf',
                'placeholder': 'Имя'
            }),
            'biography': TextInput(attrs={
                'class': 'sdf',
                'placeholder': 'Биография'
            }),
            'date_birth': NumberInput(attrs={
                'class': 'sdf',
                'placeholder': 'Год рождения'
            }),
            'date_death': NumberInput(attrs={
                'class': 'sdf',
                'placeholder': 'Год смерти'
            }),
        }