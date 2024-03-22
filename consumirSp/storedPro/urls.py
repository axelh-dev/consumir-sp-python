from django.urls import path, include
from rest_framework.documentation import include_docs_urls, get_schema_view
from rest_framework import routers, permissions
from .views import MovimientosViewSet, ClienteViewSet, cuentaViewSet, spBackupBD, spMovimientos,MonedaViewSet,CuentaViewSet, spCliente, spCuenta, regionViewSet


router = routers.DefaultRouter()
schema_view = get_schema_view(
    title="API BDbanco",
    permission_classes=(permissions.AllowAny,),
)
# Registra tus vistas con el enrutador
router.register(r'Clientes', ClienteViewSet, basename='cliente')
router.register(r'Cuentas', cuentaViewSet, basename='cuenta')
router.register(r'Movimientos', MovimientosViewSet, basename='movimiento')
router.register(r'Moneda', MonedaViewSet, basename='monedas')
router.register(r'tpocuenta', CuentaViewSet, basename='tpocuenta')
router.register(r'regionCta', regionViewSet, basename='regionCta')


urlpatterns = [
    path('v1/', include(router.urls)),  
    path('docs/', include_docs_urls(title="Api BDbanco")),
    path('spMovimiento/<cuentaOrigen>/<cuentaDestino>/<monto>/', spMovimientos, name='Ejecutar Sp' ),
    path('spCliente/<nombre>/<apellido>/<direccion>/<TipoCuenta>/<TipoMoneda>/<telefono>/<Region>/<Fecha_Nac>/', spCliente, name='spCliente'),
    path('spCuenta/<ClienteID>/<TipoCuenta>/<TipoMoneda>/<Region>', spCuenta, name='spCuenta'),
    path('spbackup/<Dir>/<TpoBack>/', spBackupBD, name='spbackup'),

]
