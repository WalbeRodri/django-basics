from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50, help_text='insira o nome')
    cpf = models.CharField(max_length=11, help_text='apenas numeros', unique=True)
    email = models.EmailField()
    data_cadastro = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True 

class Funcionario(Pessoa):
    cargo = models.CharField(max_length=20)
    meta = models.BigIntegerField()
    class Meta:
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'
    def __str__(self):
        return self.cpf

class Cliente(Pessoa):
    endereco = models.TextField(max_length=1000)
    telefone = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    def __str__(self):
        return self.endereco
    
    
class Samara(Pessoa):
    cpf = models.CharField(max_length = 11, help_text = 'apenas numeros')
    nome = models.CharField(max_length = 40)    
    
class Cinema(Filmes):
    genero = models.TextField(max_length=20)    
    duracao = models