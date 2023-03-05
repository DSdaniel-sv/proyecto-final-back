from app import api
from flask_restx import Resource
from flask import Response


health_ns = api.namespace(
    name='HealthCheck',
    decription='Servicio para validar que la aplicación esta viva',
    path='/health'
)


@health_ns.route('')
class HealthCheck(Resource):
    def get(self):
        ''' Validar que la aplicación este operativa '''
        return Response(status=200)
