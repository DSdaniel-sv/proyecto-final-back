from app import api
from flask import request
from flask_restx import Resource
from app.schemas.mercadopago_schemas import MercadopagoRequestSchema
from app.controllers.mercadopago_controller import MercadopagoController
from app.utils.mercadopago import Mercadopago

mercadopago_ns = api.namespace(
    name='Mercadopago',
    description='Rutas para la integración con mercadopago',
    path='/mercadopago'
)

request_schema = MercadopagoRequestSchema(mercadopago_ns)


@mercadopago_ns.route('/users/test')
class UserTest(Resource):
    @mercadopago_ns.expect(request_schema.createUserTest(), validate=True)
    def post(self):
        ''' Crear usuario de prueba '''
        mercadopago = Mercadopago()
        return mercadopago.createUserTest(mercadopago_ns.payload)


@mercadopago_ns.route('/webhook')
class Webhook(Resource):
    def post(self):
        ''' Recepción de pagos '''
        query = request.args.to_dict()
        payment_id = query['data.id']
        print(f'Se recibe pago del ID -> {payment_id}')
        controller = MercadopagoController()
        controller.updatePaymentStatus(payment_id)
        return {}, 200
