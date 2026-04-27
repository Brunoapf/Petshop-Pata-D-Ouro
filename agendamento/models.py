from django.db import models

from django.db import models

class clientes(models.Model):
  id_cliente = models.AutoField(primary_key=True)
  
  nome_cliente = models.CharField(
    max_length=150,
    null=False
  )
  cpf_cliente = models.CharField(
    max_length=20,
    unique=True,
    null=False
  )
  tel_cliente = models.CharField(max_length=20)
  email_cliente = models.CharField(max_length=100)
  endereco_cliente = models.TextField()

  class Meta: 
    db_table = "clientes"

class pets(models.Model):
  id_pet = models.AutoField(primary_key=True)
  
  nome_pet = models.CharField(
    max_length=100,
    null=False
  )
  especie_pet = models.CharField(
    max_length=50,
    null=False
  )
  cor_pet = models.CharField(max_length=50)
  peso_pet = models.DecimalField(max_digits=5, decimal_places=2)

  dono = models.ForeignKey(
    'clientes',
    on_delete=models.CASCADE,
    db_column='dono_id'
 )
  class Meta:
    db_table = "pets"

class servicos(models.Model): 
  id_servico = models.AutoField(primary_key=True)
  
  tipo_servico = models.CharField(
    max_length=100,
    null=False
  )
  valor_servico = models.DecimalField(
    max_digits=10, 
    decimal_places=2,
    null=False
  )
  data_hora_agenda = models.DateTimeField()

  class Meta:
    db_table = "servicos"

class produtos(models.Model):
  id_produto = models.AutoField(primary_key=True)
  
  nome_produto = models.CharField(
    max_length=100,
    null=False
  )
  categoria_produto = models.CharField(max_length=50)
  valor_produto = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    null=False
  )

  class Meta:
    db_table = "produtos"
