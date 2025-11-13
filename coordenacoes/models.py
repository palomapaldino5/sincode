from django.db import models


class TipoRelacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Conector(models.Model):
    texto = models.CharField(max_length=50)
    tipo_relacao = models.ForeignKey(TipoRelacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class Oracao(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto[:50]


class RelacaoCoordenativa(models.Model):
    oracao_1 = models.ForeignKey(Oracao, on_delete=models.CASCADE, related_name='primeira')
    conector = models.ForeignKey(Conector, on_delete=models.CASCADE)
    oracao_2 = models.ForeignKey(Oracao, on_delete=models.CASCADE, related_name='segunda')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.oracao_1} {self.conector} {self.oracao_2}"
