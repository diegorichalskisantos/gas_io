import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Pessoa


@pytest.mark.django_db
def test_create_pessoa():
    client = APIClient()
    data = {
        "nome": "João da Silva",
        "telefone": "11988888888",
        "cliente": True,
        "rua": "Rua A",
        "bairro": "Bairro B",
        "cidade": "Cidade C",
        "complemento": "Ap 101",
        "numero": "123"
    }
    response = client.post(reverse('pessoa-list'), data, format='json')

    assert response.status_code == 201
    assert Pessoa.objects.count() == 1


@pytest.mark.django_db
def test_list_pessoas(pessoa_cliente):
    client = APIClient()
    response = client.get(reverse('pessoa-list'))

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['nome'] == pessoa_cliente.nome


@pytest.mark.django_db
def test_update_pessoa(pessoa_cliente):
    client = APIClient()
    url = reverse('pessoa-detail', args=[pessoa_cliente.id])
    updated_data = {"nome": "João Atualizado"}
    response = client.patch(url, updated_data, format='json')

    assert response.status_code == 200
    assert response.data["nome"] == "João Atualizado"


@pytest.mark.django_db
def test_delete_pessoa(pessoa_cliente):
    client = APIClient()
    url = reverse('pessoa-detail', args=[pessoa_cliente.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Pessoa.objects.count() == 0


@pytest.mark.django_db
def test_create_pessoa_missing_field():
    client = APIClient()
    data = {
        # "nome" está faltando de propósito
        "telefone": "11900000000",
        "cliente": False,
        "rua": "Rua X",
        "bairro": "Centro",
        "cidade": "Cidade Y",
        "complemento": "Casa",
        "numero": "456"
    }
    response = client.post(reverse('pessoa-list'), data, format='json')

    assert response.status_code == 400
    assert "nome" in response.data
