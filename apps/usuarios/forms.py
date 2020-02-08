from django import forms

from apps.usuarios.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Userx
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'semestre', 'grupo']