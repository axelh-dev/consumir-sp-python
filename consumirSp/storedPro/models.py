from django.db import models


class Cliente(models.Model):
    id_cliente = models.IntegerField(db_column='Id_Cliente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=8, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha_nac = models.DateField(db_column='Fecha_Nac', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


class Cuenta(models.Model):
    id_cuenta = models.CharField(db_column='Id_Cuenta', primary_key=True, max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Id_Cliente', blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='Saldo', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_apertura = models.CharField(db_column='Fecha_Apertura', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_tipo_c = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='Id_Tipo_C', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey('Estcuenta', models.DO_NOTHING, db_column='Id_estado', blank=True, null=True)  # Field name made lowercase.
    id_moneda = models.ForeignKey('TipoMon', models.DO_NOTHING, db_column='Id_Moneda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cuenta'


class Estcuenta(models.Model):
    id_estado = models.CharField(db_column='Id_estado', primary_key=True, max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstCuenta'


class Movimientos(models.Model):
    id_movimiento = models.AutoField(db_column='Id_Movimiento', primary_key=True)  # Field name made lowercase.
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='Id_Cuenta')  # Field name made lowercase.
    saldo_inicial = models.DecimalField(db_column='Saldo_Inicial', max_digits=18, decimal_places=2)  # Field name made lowercase.
    saldo_final = models.DecimalField(db_column='Saldo_Final', max_digits=18, decimal_places=2)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=18, decimal_places=2)  # Field name made lowercase.
    fecha_mov = models.DateTimeField(db_column='Fecha_Mov')  # Field name made lowercase.
    id_tipomov = models.ForeignKey('TipoMov', models.DO_NOTHING, db_column='Id_TipoMov')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movimientos'


class TipoCuenta(models.Model):
    id_tipo_c = models.IntegerField(db_column='id_Tipo_C', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Cuenta'


class TipoMon(models.Model):
    id_moneda = models.CharField(db_column='Id_Moneda', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    moneda = models.CharField(db_column='Moneda', max_length=1, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Mon'


class TipoMov(models.Model):
    id_tipo_mov = models.IntegerField(db_column='Id_Tipo_Mov', primary_key=True)  # Field name made lowercase.
    descripcionmov = models.CharField(db_column='DescripcionMov', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(Estcuenta, models.DO_NOTHING, db_column='Id_estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Mov'

class Regioncta(models.Model):
    id_region = models.CharField(primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    region = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regionCta'
