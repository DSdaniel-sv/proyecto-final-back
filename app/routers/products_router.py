from app import api
from flask_restx import Resource
from app.schemas.products_schemas import ProductRequestSchema
from app.controllers.products_controller import ProductController
from flask_jwt_extended import jwt_required

product_ns = api.namespace(
    name='Productos',
    description='Rutas del modelo de productos',
    path='/products'
)

request_parser = ProductRequestSchema(product_ns)


@product_ns.route('')
@product_ns.doc(security='Bearer')
class Products(Resource):
    @jwt_required()
    @product_ns.expect(request_parser.all())
    def get(self):
        ''' Listar todos los productos '''
        query = request_parser.all().parse_args()
        controller = ProductController()
        return controller.all(query)

    @jwt_required()
    @product_ns.expect(request_parser.create(), validate=True)
    def post(self):
        ''' Crear un producto '''
        form = request_parser.create().parse_args()
        controller = ProductController()
        return controller.create(form)


@product_ns.route('/<int:id>')
@product_ns.doc(security='Bearer')
class ProductById(Resource):
    def get(self, id):
        ''' Obtener un producto por el ID '''
        controller = ProductController()
        return controller.getById(id)

    @jwt_required()
    @product_ns.expect(request_parser.update(), validate=True)
    def put(self, id):
        ''' Actualizar un producto por el ID '''
        form = request_parser.update().parse_args()
        controller = ProductController()
        return controller.update(id, form)

    def delete(self, id):
        ''' Inhabilitar un producto por el ID '''
        controller = ProductController()
        return controller.delete(id)
