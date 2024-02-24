from rest_framework import serializers
from .models import Movimientos, Cliente, Cuenta, TipoMon, TipoCuenta, Regioncta


class movimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = '__all__'
 
class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMon
        fields = '__all__'
               
 
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuenta
        fields = '__all__'
                
        
class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'        
        
class regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regioncta
        fields = '__all__'        