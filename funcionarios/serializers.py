from rest_framework import serializers
from .models import Funcionario, Cliente
import re

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'cpf', 'email', 'cargo', 'meta', 'data_cadastro')
    def validate_meta(self, valor):
        if valor in range(-100, 100): 
            return valor
        raise serializers.ValidationError('Meta fora do range')
    
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'nome',
            'cpf',
            'email',
            'data_cadastro',
            'endereco',
            'telefone',
        )
    def apenas_numeros(self, valor):
        regex_expression = r'\d*'
        if re.match(regex_expression,valor):
          return True   
        return False
    

    def validate_telefone(self, valor):
        if self.apenas_numeros(valor):
            return valor
        raise serializers.ValidationError('telefone mal formatado')


