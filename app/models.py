from . import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.JSON, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class PedidoProducto(db.Model):
    __tablename__ = 'pedido_productos'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    sucursal_id = db.Column(db.String(50), nullable=False)
    productos = db.relationship('PedidoProducto', backref='pedido', lazy=True)
    fecha = db.Column(db.DateTime, nullable=False)
