from . import ma
from .models import Producto, Pedido, PedidoProducto, User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  

class ProductoSchema(ma.SQLAlchemyAutoSchema): 
    class Meta:
        model = Producto

class PedidoProductoSchema(ma.SQLAlchemyAutoSchema): 
    class Meta:
        model = PedidoProducto

class PedidoSchema(ma.SQLAlchemyAutoSchema): 
    productos = ma.Nested(PedidoProductoSchema, many=True)

    class Meta:
        model = Pedido

class UserSchema (ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'producto', 'proceso')