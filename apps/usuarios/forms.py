from django import forms

from apps.usuarios.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput, help_text="", label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'semestre', 'grupo']