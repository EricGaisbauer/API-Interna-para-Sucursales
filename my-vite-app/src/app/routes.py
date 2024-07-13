from flask import app, request, jsonify
from flask_marshmallow import Marshmallow
from . import db
from .models import Producto, Pedido, PedidoProducto,User
from .schemas import ProductoSchema, PedidoSchema,UserSchema,TaskSchema
from datetime import datetime



producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)
pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)
user_schema = UserSchema()
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
#-----------------Metodos Productos + Pedidos --------------------------
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
    
#---------Metodos User----------------
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        result = user_schema.dump(users)
        return jsonify(result),200

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()

        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'success': False, 'message': 'Credenciales incompletas'}), 400

        username = data['username']
        password = data['password']

        # Busca el usuario por email en la base de datos
        user = User.query.filter_by(username=username).first()

        if not user or user.password != password:
            return jsonify({'success': False, 'message': 'Credenciales incorrectas'}), 401

        # Login exitoso
        return jsonify({'success': True, 'message': 'Login exitoso', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}), 200

    # Ruta para obtener un usuario[id]
    @app.route('/users/<id>', methods=['GET'])
    def get_user_id(id):
        un_usuario = User.query.get(id)
        return user_schema.jsonify(un_usuario)

    @app.route('/users/<id>',methods=['PUT'])
    def update_user(id):
        userupdate = User.query.get(id)
        data = request.get_json(force=True)
        phone = data('phone')
        password = data("password")

        userupdate.phone = phone
        userupdate.password = password
        db.session.commit()

        return user_schema.jsonify(userupdate)

    # Ruta para agregar un nuevo usuario
    @app.route('/register', methods=['POST'])
    def register_user():

        data = request.get_json(force=True)
        if request.is_json:
            username = data['username']
            email = data['email']
            phone = data['phone']
            password = data['password']
            new_user = User(username,email,phone,password)
            db.session.add(new_user)
            db.session.commit()
            return user_schema.jsonify(new_user)
        else:
            return jsonify({'message': 'La solicitud debe ser JSON'}), 400
#-------------Termino metodos User------------------------------    





    #from app.routes import init_routes

    #init_routes(app)

    class Despacho(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        producto = db.Column(db.String(70), unique=True)
        proceso = db.Column(db.String(100))
        
        def __init__(self, producto, proceso):
            self.producto = producto
            self.proceso = proceso



    @app.route('/task', methods=['POST'])
    def create_task():
        if request.is_json:
            data = request.json
            new_task = Despacho(producto=data.get('producto'), proceso=data.get('proceso'))
            db.session.add(new_task)
            db.session.commit()
            return jsonify({'message': 'Tarea creada exitosamente'}), 201
        else:
            return jsonify({'message': 'La solicitud debe ser JSON'}), 400

    @app.route('/task', methods=['GET'])
    def get_tasks():
        all_tasks = Despacho.query.all()
        result = tasks_schema.dump(all_tasks)
        return jsonify(result)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_file(path):
        return 'index.html'

    @app.route('/productos')
    def productos_view():
        return 'productos.html'

    @app.route('/pedidos')
    def pedidos_view():
        return 'pedidos.html'

    @app.route('/register')
    def register_view():
        return 'register.html'
