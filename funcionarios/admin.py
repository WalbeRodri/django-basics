from django.contrib import admin
from .models import Funcionario, Samara
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')
    
@admin.register(Samara)
class SamaraAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf')    
