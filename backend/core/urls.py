from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PessoaViewSet,
    FornecedorViewSet,
    ProdutoViewSet,
    CompraViewSet,
    VendaViewSet,
    VeiculoViewSet
)

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'veiculos', VeiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
