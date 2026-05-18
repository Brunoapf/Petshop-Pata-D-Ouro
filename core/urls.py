from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pets, name='listar_pets'),

    path('criar/', views.criar_pet, name='criar_pet'),

    path('editar/<int:id>/', views.editar_pet, name='editar_pet'),

    path('deletar/<int:id>/', views.deletar_pet, name='deletar_pet'),

    path('servicos/', views.listar_servicos, name='listar_servicos'),

    path('servicos/criar/', views.criar_servico, name='criar_servico'),

    path('servicos/editar/<int:id>/', views.editar_servico, name='editar_servico'),

    path('servicos/deletar/<int:id>/', views.deletar_servico, name='deletar_servico'),

    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),

    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),

    path('agendamentos/editar/<int:id>/', views.editar_agendamento, name='editar_agendamento'),

    path('agendamentos/deletar/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),
]