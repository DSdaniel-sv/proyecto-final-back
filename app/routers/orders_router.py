from app import api
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.orders_schemas import OrderRequestSchema
from app.controllers.orders_controller import OrderController

order_ns = api.namespace(
    name='Ordenes de Compra',
    description='Rutas para el modelo de Ordenes',
    path='/orders'
)

request_schema = OrderRequestSchema(order_ns)


@order_ns.route('')
@order_ns.doc(security='Bearer')
class Order(Resource):
    @jwt_required()
    @order_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de un pedido '''
        controller = OrderController()
        return controller.create(order_ns.payload)
