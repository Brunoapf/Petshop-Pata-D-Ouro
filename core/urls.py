from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # LOGIN
    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    # LOGOUT
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # DASHBOARD
    path('home/', views.dashboard, name='dashboard'),
    
    # PETS
    path('pets/', views.listar_pets, name='listar_pets'),
    path('pets/criar/', views.criar_pet, name='criar_pet'),
    path('pets/editar/<int:id>/', views.editar_pet, name='editar_pet'),
    path('deletar/<int:id>/', views.deletar_pet, name='deletar_pet'),

    # SERVIÇOS
    path('servicos/', views.listar_servicos, name='listar_servicos'),
    path('servicos/criar/', views.criar_servico, name='criar_servico'),
    path('servicos/editar/<int:id>/', views.editar_servico, name='editar_servico'),
    path('servicos/deletar/<int:id>/', views.deletar_servico, name='deletar_servico'),

    # AGENDAMENTOS
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),
    path('agendamentos/editar/<int:id>/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamentos/deletar/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),
]