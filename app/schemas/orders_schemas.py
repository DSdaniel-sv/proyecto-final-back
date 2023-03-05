from flask_restx import fields


class OrderRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Order Create', {
            'date_shopping': fields.Date(required=True)
        })
