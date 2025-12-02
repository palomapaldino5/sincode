from django import forms
from django.contrib.auth.models import User
from associados.models import Associado


class AssociadosForm(forms.ModelForm):
    usuario = forms.CharField(
        label="Usuário",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        })
    )

    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    confirmar_senha = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Associado
        fields = [
            'nome_completo',
            'nome_social',
            'data_nascimento',
            'genero',
            'genero_outro'
        ]
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'genero_outro': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned = super().clean()
        s1 = cleaned.get("senha")
        s2 = cleaned.get("confirmar_senha")

        if s1 != s2:
            self.add_error("confirmar_senha", "As senhas não coincidem.")

        return cleaned
