from django.contrib import admin
from .models import Funcionario,Kassiooo
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

@admin.register(Kassiooo)
class KassioooAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','end')