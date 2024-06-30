from flask import request, jsonify
from . import db
from .models import Producto, Pedido, PedidoProducto
from .schemas import ProductoSchema, PedidoSchema
from datetime import datetime

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

def init_routes(app):
    @app.route('/api/productos', methods=['GET'])
    def get_productos():
        productos = Producto.query.all()
        productos_json = productos_schema.dump(productos) 
        return jsonify(productos_json)

    @app.route('/api/productos/<int:id>', methods=['GET'])
    def get_producto(id):
        producto = Producto.query.get(id)
        if producto is None:
            return jsonify({"message": "Producto no encontrado"}), 404
        producto_json = producto_schema.dump(producto)  
        return jsonify(producto_json)

    @app.route('/api/productos', methods=['POST'])
    def add_producto():
        data = request.get_json()
        new_producto = Producto(
            codigo=data['codigo'],
            nombre=data['nombre'],
            marca=data['marca'],
            precio=data['precio'],
            stock=data['stock']
        )
        db.session.add(new_producto)
        db.session.commit()
        producto_json = producto_schema.dump(new_producto)
        return jsonify(producto_json)

    @app.route('/api/pedidos', methods=['POST'])
    def create_pedido():
        data = request.get_json()
        new_pedido = Pedido(
            sucursal_id=data['sucursal_id'],
            fecha=datetime.utcnow()
        )
        db.session.add(new_pedido)
        db.session.commit()
        for producto in data['productos']:
            new_pedido_producto = PedidoProducto(
                producto_id=producto['producto_id'],
                cantidad=producto['cantidad'],
                pedido_id=new_pedido.id
            )
            db.session.add(new_pedido_producto)
        db.session.commit()
        pedido_json = pedido_schema.dump(new_pedido) 
        return jsonify(pedido_json)

    @app.route('/api/pedidos', methods=['GET'])
    def get_pedidos():
        pedidos = Pedido.query.all()
        pedidos_json = pedidos_schema.dump(pedidos)
        return jsonify(pedidos_json)
    
    @app.route('/api/pedidos/<int:id>', methods=['GET'])
    def get_pedido(id):
        pedido = Pedido.query.get(id)
        if pedido is None:
            return jsonify({"message": "Pedido no encontrado"}), 404
        pedido_json = pedido_schema.dump(pedido)  
        return jsonify(pedido_json)
    
    @app.route('/api/productos/<int:id>', methods=['PUT'])
    def update_producto(id):
        producto = Producto.query.get(id)
        if producto is None:
            return jsonify({"message": "Producto no encontrado"}), 404

        data = request.get_json()
        producto.codigo = data['codigo']
        producto.nombre = data['nombre']
        producto.marca = data['marca']
        producto.precio = data['precio']
        producto.stock = data['stock']

        db.session.commit()
        producto_json = producto_schema.dump(producto)
        return jsonify(producto_json)

    @app.route('/api/productos/<int:id>', methods=['DELETE'])
    def delete_producto(id):
        producto = Producto.query.get(id)
        if producto is None:
            return jsonify({"message": "Producto no encontrado"}), 404

        db.session.delete(producto)
        db.session.commit()
        return jsonify({"message": "Producto eliminado correctamente"}), 200
