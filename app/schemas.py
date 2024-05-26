from . import ma
from .models import Producto, Pedido, PedidoProducto
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  

class ProductoSchema(SQLAlchemyAutoSchema): 
    class Meta:
        model = Producto

class PedidoProductoSchema(SQLAlchemyAutoSchema): 
    class Meta:
        model = PedidoProducto

class PedidoSchema(SQLAlchemyAutoSchema): 
    productos = ma.Nested(PedidoProductoSchema, many=True)

    class Meta:
        model = Pedido
