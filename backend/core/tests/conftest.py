import pytest
from core.models import Fornecedor, Produto, Pessoa, Veiculo


@pytest.fixture
def fornecedor():
    return Fornecedor.objects.create(
        nome="Rafael Dalspin",
        telefone="11999999999",
        rua="Rua do Fornecedor",
        numero="24",
        bairro="Centro",
        cidade="Cidade",
        complemento="Garagem"
    )


@pytest.fixture
def produto():
    return Produto.objects.create(
        nome="Botijão P13",
        capacidade=13,
        valor_venda="100.00"
    )


@pytest.fixture
def pessoa_cliente():
    return Pessoa.objects.create(
        nome="João da Silva",
        telefone="11988888888",
        cliente=True,
        rua="Rua A",
        numero="123",
        bairro="Bairro B",
        cidade="Cidade C",
        complemento="Ap 101"
    )


@pytest.fixture
def veiculo():
    return Veiculo.objects.create(
        placa="XYZ1234",
        modelo="Fiorino",
        capacidade_carga="200.50"
    )

