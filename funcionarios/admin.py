from django.contrib import admin
from .models import Funcionario, Eduardo, Dominique, Kassiooo, Heroi_Vicente, Diego
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

@admin.register(Diego)
class DiegoAdmin(admin.ModelAdmin):
    list_display = ('nome','genero','idade')
    
@admin.register(Kassiooo)
class KassioooAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','end')
    
@admin.register(Eduardo)
class EduardoAdmin(admin.ModelAdmin):
    list_display = ('caracteristicas',)
    
@admin.register(Dominique)
class DominiqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'cor')

@admin.register(Heroi_Vicente)
class HeroiVicenteAdmin(admin.ModelAdmin):
    list_display = ('superpoder', 'nivel')
