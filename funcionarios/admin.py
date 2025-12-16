from django.contrib import admin
from .models import Funcionario, Diego
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

@admin.register(Diego)
class DiegoAdmin(admin.ModelAdmin):
    list_display = ('nome','genero','idade')