from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data): 
        if  not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 Dígitos'})              
        if not Verificando_se_eh_letra(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números nesse campo'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})
        
        if celular_valido(data['celular']):
             raise serializers.ValidationError({'celular':'O celular deve ter pelo menos 11 dígitos '})
        
        return data