import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Fornecedor


@pytest.mark.django_db
def test_create_fornecedor():
    client = APIClient()
    data = {
        "nome": "Fornecedor Alpha",
        "telefone": "11999999999",
        "rua": "Rua Principal",
        "numero": "100",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "complemento": "Galpão"
    }
    response = client.post(reverse('fornecedor-list'), data, format='json')

    assert response.status_code == 201
    assert Fornecedor.objects.count() == 1


@pytest.mark.django_db
def test_list_fornecedores(fornecedor):
    client = APIClient()
    response = client.get(reverse('fornecedor-list'))

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['nome'] == fornecedor.nome
    
    


@pytest.mark.django_db
def test_update_fornecedor(fornecedor):
    client = APIClient()
    url = reverse('fornecedor-detail', args=[fornecedor.id])
    update_data = {"nome": "Fornecedor Atualizado"}
    response = client.patch(url, update_data, format='json')

    assert response.status_code == 200
    assert response.data["nome"] == "Fornecedor Atualizado"


@pytest.mark.django_db
def test_delete_fornecedor(fornecedor):
    client = APIClient()
    url = reverse('fornecedor-detail', args=[fornecedor.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Fornecedor.objects.count() == 0
