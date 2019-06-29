from flask import Blueprint
from flask_restful import Api

from resources.Category import CategoryResource
from resources.Comments import CommentResource
from resources.Hello import Hello

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route

api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
