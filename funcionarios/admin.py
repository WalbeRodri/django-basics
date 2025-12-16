from django.contrib import admin
from .models import Funcionario, Eduardo

# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

@admin.register(Eduardo)
class EduardoAdmin(admin.ModelAdmin):
    list_display = ('caracteristicas')
    
    
   