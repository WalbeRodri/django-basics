from django.contrib import admin
from .models import Funcionario, Eduardo, Dominique
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')
  
    
@admin.register(Dominique)
class DominiqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'cor')