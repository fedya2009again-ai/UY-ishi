from django import forms
from .models import Phone


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500)


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

        labels = {
            'name': 'Telefon nomi',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Telefon nomini kiriting'
            }),
        }
