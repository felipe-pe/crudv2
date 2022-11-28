from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("crud", views.crud, name='crud'),
    path("gera_relatorio", views.gera_relatorio, name="gera_relatorio"),
    path("voos", views.voos.as_view(), name="voos"),
    path("status", views.status, name="status"),
    path("criar_voo_chegada", views.criar_voo_chegada, name="criar_voo_chegada"),
    path("criar_voo_partida", views.criar_voo_partida, name="criar_voo_partida"),
    path("editar", views.editar, name="editar"),
    path("ler_voo", views.ler_voo, name="ler_voo"),
    path("deletar", views.deletar, name="deletar"),
    path("relatorio_chegadas", views.relatorio_chegadas, name="relatorio_chegadas"),
    path("relatorio_partidas", views.relatorio_partidas, name="relatorio_partidas"),
]