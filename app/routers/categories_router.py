from app import api
from flask import request
from flask_restx import Resource
from app.schemas.categories_schemas import CategoriesRequestSchema
from app.controllers.categories_controller import CategoriesController
from flask_jwt_extended import jwt_required


category_ns = api.namespace(
    name='Categorias de Producto',
    description='Rutas del modelo de Categorias',
    path='/categories'
)

request_schema = CategoriesRequestSchema(category_ns)


@category_ns.route('')
@category_ns.doc(security='Bearer')
class Categories(Resource):
    @jwt_required()
    @category_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todas las categorias '''
        query = request_schema.all().parse_args()
        controller = CategoriesController()
        return controller.all(query)

    @jwt_required()
    @category_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de Categoria '''
        controller = CategoriesController()
        return controller.create(request.json)


@category_ns.route('/<int:id>')
@category_ns.doc(security='Bearer')
class CategoryById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una categorias por el ID '''
        controller = CategoriesController()
        return controller.getById(id)

    @jwt_required()
    @category_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una categorias por el ID '''
        controller = CategoriesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Inhabilitar una categorias por el ID '''
        controller = CategoriesController()
        return controller.delete(id)
