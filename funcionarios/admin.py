from django.contrib import admin
from .models import Funcionario, Rayanne
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

@admin.register(Rayanne)
class RayanneAdmin(admin.ModelAdmin):
    list_display = ('nacionalidade', 'altura', 'cor_do_cabelo', 'hobbies')