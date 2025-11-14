from django.db import models

class UnidadeCoordenada(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto[:50]


class TipoRelacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class ConectorCoordenativo(models.Model):
    texto = models.CharField(max_length=50)
    tipo_relacao = models.ForeignKey(TipoRelacao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.texto} ({self.tipo_relacao.nome})"


class RelacaoCoordenativa(models.Model):
    unidade_1 = models.ForeignKey(UnidadeCoordenada, on_delete=models.CASCADE, related_name='relacao_unidade_1')
    conector = models.ForeignKey(ConectorCoordenativo, on_delete=models.CASCADE)
    unidade_2 = models.ForeignKey(UnidadeCoordenada, on_delete=models.CASCADE, related_name='relacao_unidade_2')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.unidade_1} {self.conector.texto} {self.unidade_2}"
