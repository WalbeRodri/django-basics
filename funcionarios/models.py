from django.db import models 
from .constantes import SUPERPODER_CHOICES

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

class Kassiooo(Pessoa):
    end=models.TextField(max_length=1000)
    meta = models.BigIntegerField()
    cargo = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
    
    
class Samara(Pessoa):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome 
    cpf = models.CharField(max_length = 11, help_text = 'apenas numeros')
    nome = models.CharField(max_length = 40)    
    
class Pedro(Pessoa):
    saldo = models.IntegerField()
    def __str__(self):
        return f'{self.name} = {self.saldo}'
    
class Dominique(Pessoa):
    idade = models.IntegerField( help_text='Insira sua idade')
    cor = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Domi'      
    def __str__(self):
        return self.nome

class Eduardo(Pessoa):
    caracteristicas = models.TextField(max_length=1000)   
    
    def __str__(self):
        return self.caracteristicas 
    

class Rayanne(Pessoa):
    nacionalidade = models.CharField(max_length=50)
    altura = models.CharField(max_length=50)
    cor_do_cabelo = models.CharField(max_length=50)
    hobbies = models.TextField(max_length=500)
    class Meta:
        verbose_name = 'rayanne'
    def __str__(self):
        return self.nacionalidade

class Heroi_Vicente(Pessoa):
    superpoder = models.CharField(verbose_name='Superpoder', max_length=120, choices=SUPERPODER_CHOICES)
    nivel = models.IntegerField(verbose_name='Nível')
    def __str__(self):
        return f"Herói com {self.superpoder}"
    
class Cinema(Pessoa):
    terror = models.CharField(max_length=20)
    comedia = models.CharField(max_length=20)
    aventura = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.terror}'

class Robert(Pessoa):
    caracteristicas = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.name} = {self.caracteristicas}'

class Conta(models.Model):
    numero_conta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contas')
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'conta'
        verbose_name_plural = 'contas'
    def __str__(self):
        return self.numero_conta

class Abraao(Pessoa):
    formacao = models.CharField(max_length=100)
    profissao = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'abraao'
    def __str__(self):
        return self.formacao
    
class Diego(Pessoa):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=1)
    idade = models.IntegerField()
    
    def __str__(self):
        return self.nome
