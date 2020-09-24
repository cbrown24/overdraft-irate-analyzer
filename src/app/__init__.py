from flask_restplus import Api
from flask import Blueprint

# from .api 

from .main.controller.overdraft_controller import api as overdraft_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Overdraft transaction summary',
          version='1.0',
          description='a flask app with a restplus web service',
          )

api.add_namespace(overdraft_ns, path='/overdraft')