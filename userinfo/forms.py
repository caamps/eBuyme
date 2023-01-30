from django.forms import ModelForm, TextInput, FileInput, NumberInput
from main.models import User


class EditUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].widget.attrs.update({
            'class': 'form-control'
        })
    class Meta:
        model = User
        fields = ['nome', 'estado', 'cidade', 'rua', 'bairro', 'numero', 'cep', 'foto']
        widgets = {
            'nome': TextInput(attrs={
                'class': 'form-control',
            }),
            'cidade': TextInput(attrs={
                'class': 'form-control',
            }),
            'rua': TextInput(attrs={
                'class': 'form-control',
            }),
            'bairro': TextInput(attrs={
                'class': 'form-control',
            }),
            'numero': NumberInput(attrs={
                'class': 'form-control',
            }),
            'cep': TextInput(attrs={
                'class': 'form-control',
            }),
            'foto': FileInput(attrs={
                'class': 'form-control',
                'onChange': 'loadFile(event)'
            }),
            }        
