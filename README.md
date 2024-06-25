# API Interna para Sucursales

## Descripción
La API Interna para Sucursales es una API RESTful desarrollada en Flask que permite la gestión de productos y pedidos en distintas sucursales. Ofrece funcionalidades CRUD (Crear, Leer, Actualizar y Borrar) para administrar la información de manera eficiente.

## Tecnologías Utilizadas
- **Python**
- **Flask**
- **SQLAlchemy**
- **Marshmallow**
- **MySQL**
- **MySQL Workbench**
- **Postman**

## Endpoints Principales
1. **Productos**
   - `GET /api/productos`: Obtener la lista de todos los productos.
   - `GET /api/productos/{id}`: Obtener un producto específico por su ID.
   - `POST /api/productos`: Crear un nuevo producto.
   - `PUT /api/productos/{id}`: Actualizar un producto existente por su ID.
   - `DELETE /api/productos/{id}`: Eliminar un producto por su ID.

2. **Pedidos**
   - `GET /api/pedidos`: Obtener la lista de todos los pedidos.
   - `GET /api/pedidos/{id}`: Obtener un pedido específico por su ID.
   - `POST /api/pedidos`: Crear un nuevo pedido.

## Configuración
1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/API-Interna-para-Sucursales.git
    cd API-Interna-para-Sucursales
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configura la base de datos:
    - Crea una base de datos MySQL y ejecuta el script `ferreteria.sql` ubicado en la carpeta `database`.

4. Ejecuta la aplicación:
    ```bash
    python main.py
    ```

## Documentación de Postman
La documentación completa de la API está disponible en [Postman](https://documenter.getpostman.com/view/35033767/2sA3QngZ7N).

## Estructura del Proyecto
```plaintext
API-Interna-para-Sucursales/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
├── database/
│   └── ferreteria.sql
├── venv/
├── requirements.txt
├── run.py
└── README.md
```

## Contacto
Puedes contactarme a través de [mi correo](ericgaisbauer@gmail.com) o seguirme en [LinkedIn](https://www.linkedin.com/in/eric-gaisbauer).

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejoras y correcciones.
