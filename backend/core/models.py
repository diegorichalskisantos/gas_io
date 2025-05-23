from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.DecimalField(max_digits=5, decimal_places=2)  # ex: 13.00 kg
    valor_venda = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.capacidade}kg"


class Veiculo(models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=50)
    capacidade_carga = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.placa


class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_compra = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.produto} em {self.data_compra}"


class Venda(models.Model):
    cliente = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_venda = models.DateField()

    def __str__(self):
        return f"Venda para {self.cliente} em {self.data_venda}"
