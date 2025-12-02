from django.db import models
from django.contrib.auth.models import User

class Associado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nome_completo = models.CharField(max_length=150)
    nome_social = models.CharField(max_length=150, blank=True, null=True)

    data_nascimento = models.DateField()

    genero = models.CharField(
        max_length=50,
        choices=[
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
            ('Outro', 'Outro'),
            ('Prefiro não informar', 'Prefiro não informar'),
        ]
    )
    genero_outro = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome_completo
