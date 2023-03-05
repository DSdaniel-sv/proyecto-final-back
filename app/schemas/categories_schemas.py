from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.categories_model import CategoryModel


class CategoriesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('Category Create', {
            'name': fields.String(required=True, max_length=120)
        })

    def update(self):
        return self.namespace.model('Category Update', {
            'name': fields.String(required=False, max_length=120)
        })


class CategoriesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        ordered = True
