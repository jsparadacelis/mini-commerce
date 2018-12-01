from django import forms
from django.contrib.auth.models import User
from .models import Client

class LoginForm(forms.Form):
    username = forms.CharField(label='usuario', max_length=15)
    password = forms.CharField(
        label='contraseña',
        min_length = 6, 
        max_length=15,
        widget=forms.PasswordInput()
    )

class SignUpForm(forms.Form):
    username = forms.CharField(label='usuario', max_length=15)
    password = forms.CharField(
        label='contraseña',
        min_length = 6, 
        max_length=15,
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label='confirmar contraseña',
        min_length = 6, 
        max_length=15,
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(label='correo electrónico')
    terminal_id = forms.CharField(label='terminal', max_length=20)

    def clean_username(self):

        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username = username) 
        username_taken = username_taken.exists()

        if username_taken:
            raise forms.ValidationError('El usuario ya existe')
        return username


    def clean(self):

        data = super().clean()
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data

    
    def save(self):
        data = self.cleaned_data
        data.pop('confirm_password')

        user = User.objects.create_user(
            data["username"],
            data["email"],
            data["password"]
        )

        user.save()

        client = Client.objects.create(
            user = user,
            terminal = data["terminal_id"]
        )
        
        client.save()


                   
    
