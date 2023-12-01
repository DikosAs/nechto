from django import forms
from .models import *
from django.core.exceptions import ValidationError

class NewGameForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ('gameID', 'gamePassword', 'gameAdmin')
        widgets = {
            'gameID': forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            'gamePassword': forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            'gameAdmin': forms.TextInput(attrs={"class": "form-control form-control-lg"})
        }

    # def clean_title(self):
    #     data = self.cleaned_data['gameID']
    #     if data and data.startswith("?"):
    #         raise ValidationError("Вопросительный знак в заголовке")
    #     return data