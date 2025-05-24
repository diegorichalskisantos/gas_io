import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Compra


@pytest.mark.django_db
def test_create_compra(fornecedor, produto):
    client = APIClient()
    data = {
        "fornecedor": fornecedor.id,
        "produto": produto.id,
        "valor_total": "80.00",
        "data_compra": "2024-01-01"
    }
    response = client.post(reverse('compra-list'), data, format='json')
    
    print(response)

    assert response.status_code == 201
    assert Compra.objects.count() == 1


@pytest.mark.django_db
def test_list_compra(fornecedor, produto):
    Compra.objects.create(
        fornecedor=fornecedor,
        produto=produto,
        valor_total="80.00",
        data_compra="2024-01-01"
    )

    client = APIClient()
    response = client.get(reverse('compra-list'))

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_update_compra(fornecedor, produto):
    compra = Compra.objects.create(
        fornecedor=fornecedor,
        produto=produto,
        valor_total="80.00",
        data_compra="2024-01-01"
    )

    client = APIClient()
    url = reverse('compra-detail', args=[compra.id])
    update_data = {"valor_total": "90.00"}
    response = client.patch(url, update_data, format='json')

    assert response.status_code == 200
    assert response.data["valor_total"] == "90.00"


@pytest.mark.django_db
def test_delete_compra(fornecedor, produto):
    compra = Compra.objects.create(
        fornecedor=fornecedor,
        produto=produto,
        valor_total="80.00",
        data_compra="2024-01-01"
    )

    client = APIClient()
    url = reverse('compra-detail', args=[compra.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Compra.objects.count() == 0
