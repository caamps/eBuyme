from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from main.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = User
        fields = ['email', 'username', 'nome', 'password1', 'password2']
        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "name@example.com"
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "exemplo_34"
            }),
            'nome': TextInput(attrs={
                'class': 'form-control',
            })
        }

class ChangePassForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })
        
    class Meta:
        model = User
        fields = ['password1', 'password2']
