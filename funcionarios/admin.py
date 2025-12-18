from django.contrib import admin
from .models import Funcionario, Eduardo, Dominique, Kassiooo, Heroi_Vicente, Diego, Rayanne
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')
    
@admin.register(Samara)
class SamaraAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf')    
