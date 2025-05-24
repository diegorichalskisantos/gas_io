import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Venda


@pytest.mark.django_db
def test_create_venda(pessoa_cliente, produto, veiculo):
    client = APIClient()
    data = {
        "cliente": pessoa_cliente.id,
        "produto": produto.id,
        "veiculo": veiculo.id,
        "valor": "100.00",
        "data_venda": "2024-01-01"
    }
    response = client.post(reverse('venda-list'), data, format='json')

    assert response.status_code == 201
    assert Venda.objects.count() == 1
    assert Venda.objects.first().valor == 100.00


@pytest.mark.django_db
def test_list_vendas(pessoa_cliente, produto, veiculo):
    Venda.objects.create(
        cliente=pessoa_cliente,
        produto=produto,
        veiculo=veiculo,
        valor="100.00",
        data_venda="2024-01-01"
    )

    client = APIClient()
    response = client.get(reverse('venda-list'))

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_update_venda(pessoa_cliente, produto, veiculo):
    venda = Venda.objects.create(
        cliente=pessoa_cliente,
        produto=produto,
        veiculo=veiculo,
        valor="100.00",
        data_venda="2024-01-01"
    )

    client = APIClient()
    url = reverse('venda-detail', args=[venda.id])
    data = {"valor": "110.00"}
    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data["valor"] == "110.00"


@pytest.mark.django_db
def test_delete_venda(pessoa_cliente, produto, veiculo):
    venda = Venda.objects.create(
        cliente=pessoa_cliente,
        produto=produto,
        veiculo=veiculo,
        valor="100.00",
        data_venda="2024-01-01"
    )

    client = APIClient()
    url = reverse('venda-detail', args=[venda.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Venda.objects.count() == 0
