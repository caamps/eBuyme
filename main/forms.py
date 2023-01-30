from django.forms import ModelForm, TextInput, NumberInput
from .models import User

class EditEnderecoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].widget.attrs.update({
            'class': 'form-control'
        })
    class Meta:
        model = User
        fields = ['estado', 'cidade', 'rua', 'bairro', 'numero', 'cep']
        widgets = {
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
        }
