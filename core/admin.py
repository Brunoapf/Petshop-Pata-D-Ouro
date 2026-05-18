from django.contrib import admin
# Register your models here.
from .models import Cliente, Pet, Servico, Agendamento

# Aqui vcs avisa ao Django -  "Mostre essas tabelas no meu painel"
admin.site.register(Cliente)
admin.site.register(Pet)
admin.site.register(Servico)
admin.site.register(Agendamento)
