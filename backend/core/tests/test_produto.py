import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Produto


@pytest.mark.django_db
def test_create_produto():
    client = APIClient()
    data = {
        "nome": "Botijão P13",
        "capacidade": 13,
        "valor_venda": "100.00"
    }
    response = client.post(reverse('produto-list'), data, format='json')

    assert response.status_code == 201
    assert Produto.objects.count() == 1
    assert Produto.objects.first().nome == "Botijão P13"


@pytest.mark.django_db
def test_list_produtos(produto):
    client = APIClient()
    response = client.get(reverse('produto-list'))

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['nome'] == produto.nome


@pytest.mark.django_db
def test_update_produto(produto):
    client = APIClient()
    url = reverse('produto-detail', args=[produto.id])
    update_data = {"valor_venda": "110.00"}
    response = client.patch(url, update_data, format='json')

    assert response.status_code == 200
    assert response.data["valor_venda"] == "110.00"


@pytest.mark.django_db
def test_delete_produto(produto):
    client = APIClient()
    url = reverse('produto-detail', args=[produto.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Produto.objects.count() == 0
