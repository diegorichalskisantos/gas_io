import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Veiculo


@pytest.mark.django_db
def test_create_veiculo():
    client = APIClient()
    data = {
        "placa": "XYZ1234",
        "modelo": "Fiorino",
        "capacidade_carga": "200.50"
    }
    response = client.post(reverse('veiculo-list'), data, format='json')

    assert response.status_code == 201
    assert Veiculo.objects.count() == 1
    veiculo = Veiculo.objects.first()
    assert veiculo.placa == "XYZ1234"
    assert veiculo.modelo == "Fiorino"


@pytest.mark.django_db
def test_list_veiculo(veiculo):
    client = APIClient()
    response = client.get(reverse('veiculo-list'))

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['placa'] == veiculo.placa
    assert response.data[0]['modelo'] == veiculo.modelo


@pytest.mark.django_db
def test_update_veiculo(veiculo):
    client = APIClient()
    url = reverse('veiculo-detail', args=[veiculo.id])
    data = {"modelo": "HR-Bongo"}
    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data["modelo"] == "HR-Bongo"


@pytest.mark.django_db
def test_delete_veiculo(veiculo):
    client = APIClient()
    url = reverse('veiculo-detail', args=[veiculo.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Veiculo.objects.count() == 0
