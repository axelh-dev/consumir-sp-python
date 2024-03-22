from django.shortcuts import render ## Se Usa para devolver un pantilla en html
from .models import Movimientos, Cliente, Cuenta, TipoMon, TipoCuenta, Regioncta
from .serializer import  movimientosSerializer, clienteSerializer, cuentaSerializer, MonedaSerializer, CuentaSerializer, regionSerializer
from rest_framework import viewsets
from django.http import JsonResponse

# Ejecuta el SP
from django.db import connection
cursor = connection.cursor()

def spBackupBD(request, Dir, TpoBack ):
    #
    if Dir is None or TpoBack is None:
        return JsonResponse({'error': 'Se requieren todos los parámetros'}, status=400)
    try:
        with connection.cursor() as cursor:
            cursor.execute('EXEC DBBackupFull_banco @Dir=%s, @TpoBack=%s', [Dir, TpoBack])
            if cursor.description is not None:
                results = cursor.fetchall()
            else:
                results = None
        response_data = {
            'message': 'BackUp Exitosa',
            'results': results,
        }
        return JsonResponse(response_data)
    except Exception as e:
        error_message = str(e)
        start_index = error_message.find("ERROR:")
        if start_index != -1:
            error_message = error_message[start_index:]
        return JsonResponse({'error': error_message, 'results': None}, status=500)



def spMovimientos(request, cuentaOrigen, cuentaDestino, monto):
    #
    if cuentaOrigen is None or cuentaDestino is None or monto is None:
        return JsonResponse({'error': 'Se requieren todos los parámetros'}, status=400)
    try:
        with connection.cursor() as cursor:
            cursor.execute('EXEC sp_movimiento @Monto=%s, @CuentaOrigen=%s, @CuentaDestino=%s', [monto, cuentaOrigen, cuentaDestino])
            if cursor.description is not None:
                results = cursor.fetchall()
            else:
                results = None
        response_data = {
            'message': 'Transacción exitosa',
            'results': results,
        }
        return JsonResponse(response_data)
    except Exception as e:
        error_message = str(e)
        start_index = error_message.find("ERROR:")
        if start_index != -1:
            error_message = error_message[start_index:]
        return JsonResponse({'error': error_message, 'results': None}, status=500)
    
def spCliente(request, nombre, apellido, direccion, TipoCuenta, TipoMoneda, telefono, Region, Fecha_Nac):

    if None in [nombre, apellido, direccion, TipoCuenta, TipoMoneda, telefono,  Fecha_Nac, Region]:
        return JsonResponse({'error': 'Se requieren todos los parámetros'}, status=400)

    try:
        with connection.cursor() as cursor:
            # Llamamos al SP
            cursor.execute('EXEC nuevoCliente @nombre=%s, @apellido=%s, @direccion=%s, @TipoCuenta=%s, @TipoMoneda=%s, @telefono=%s, @Region=%s, @Fecha_Nac=%s',
                           [nombre, apellido, direccion, TipoCuenta, TipoMoneda, telefono, Region, Fecha_Nac])

            if cursor.description is not None:
                results = cursor.fetchall()
            else:
                results = None

        response_data = {
            'message': 'Transacción exitosa',
            'results': results,
        }
        return JsonResponse(response_data)
    except Exception as e:
        error_message = str(e)
        start_index = error_message.find("ERROR:")
        if start_index != -1:
            error_message = error_message[start_index:]
        return JsonResponse({'error': error_message, 'results': None}, status=500)

def spCuenta(request, ClienteID, TipoCuenta, TipoMoneda, Region):
    #
    if ClienteID is None or TipoCuenta is None or TipoMoneda is None:
        return JsonResponse({'error': 'Se requieren todos los parámetros'}, status=400)

    try:
        with connection.cursor() as cursor:
            cursor.execute('EXEC crearCuenta @ClienteID=%s, @TipoCuenta=%s, @TipoMoneda=%s , @Region=%s', [ClienteID, TipoCuenta, TipoMoneda, Region])
            if cursor.description is not None:
                results = cursor.fetchall()
            else:
                results = None
        response_data = {
            'message': 'Transacción exitosa',
            'results': results,
        }
        return JsonResponse(response_data)
    except Exception as e:
         # Obtener solo el mensaje de error específico
        error_message = str(e)
        start_index = error_message.find("ERROR:")
        if start_index != -1:
            error_message = error_message[start_index:]
        return JsonResponse({'error': error_message, 'results': None}, status=500)
    
# Create your views here.
class MovimientosViewSet(viewsets.ModelViewSet):
    queryset = Movimientos.objects.all()
    serializer_class = movimientosSerializer

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = TipoCuenta.objects.all()
    serializer_class = CuentaSerializer

    
class MonedaViewSet(viewsets.ModelViewSet):
    queryset = TipoMon.objects.all()
    serializer_class = MonedaSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer

class cuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = cuentaSerializer



class regionViewSet(viewsets.ModelViewSet):
    queryset = Regioncta.objects.all()
    serializer_class = regionSerializer
