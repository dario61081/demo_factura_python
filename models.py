from datetime import datetime

from sqlalchemy import Column, INTEGER, VARCHAR, DATE, ForeignKey, NUMERIC, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

fecha = VARCHAR(10)  # format YYYY-MM-DD


class BaseMain:
    codigo = Column(INTEGER, primary_key=True, autoincrement=True)


BASE = declarative_base(cls=BaseMain)


class ModelSucursal(BASE):
    __tablename__ = 'sucursales'
    nombre = Column(VARCHAR(100), index=True)
    direccion = Column(VARCHAR(100), index=True)

    def setup(self):
        return [
            ModelSucursal(nombre='Sucursal 001', direccion='Direccion 1'),
            ModelSucursal(nombre='Sucursal 002', direccion='Direccion 2')
        ]


class ModelCaja(BASE):
    __tablename__ = 'cajas'
    codigo_sucursal = Column(INTEGER, ForeignKey('sucursales.codigo'), index=True)
    nombre = Column(VARCHAR(100), index=True)

    def setup(self):
        return [
            ModelCaja(nombre='Caja 001', codigo_sucursal=1),
            ModelCaja(nombre='Caja 002', codigo_sucursal=2),
        ]


class ModelTimbrado(BASE):
    __tablename__ = 'timbrados'
    numero = Column(VARCHAR(8), unique=True)
    codigo_caja = Column(INTEGER, ForeignKey('cajas.codigo'), index=True)
    fecha_inicio = Column(fecha, index=True)
    fecha_vencimiento = Column(fecha, index=True)
    valor_inicial = Column(INTEGER, index=True)
    valor_final = Column(INTEGER, index=True)
    posicion = Column(INTEGER, index=True)

    def setup(self):
        return [
            ModelTimbrado(numero='00000001', codigo_caja=1, fecha_inicio='2020-01-01', fecha_vencimiento='2020-12-31',
                          valor_inicial=1, valor_final=500, posicion=1),
            ModelTimbrado(numero='00000002', codigo_caja=2, fecha_inicio='2020-01-01', fecha_vencimiento='2020-12-31',
                          valor_inicial=1500, valor_final=2000, posicion=1560),
        ]


class ModelFactura(BASE):
    __tablename__ = 'facturas'
    fecha = Column(TEXT, index=True)
    razon_social = Column(VARCHAR(100), index=True)
    ruc = Column(VARCHAR(20), index=True)
    direccion = Column(VARCHAR(100), index=True)
    numero = Column(VARCHAR(20), index=True)
    codigo_timbrado = Column(INTEGER, ForeignKey('timbrados.codigo'), index=True)

    # items = relationship('ModelFacturaItem', back_populates='facturas', primaryjoin='ModelFactura.codigo == ModelFacturaItem.codigo_factura')


class ModelFacturaItem(BASE):
    __tablename__ = 'facturas_detalles'
    codigo_factura = Column(INTEGER, ForeignKey('facturas.codigo', onupdate='RESTRICT', ondelete='RESTRICT'),
                            index=True)
    cantidad = Column(NUMERIC(18, 2), index=True)
    descripcion = Column(VARCHAR(100), index=True)
    precio_unitario = Column(NUMERIC(18, 2), index=True)
    subtotal = Column(NUMERIC(18, 2), index=True)
