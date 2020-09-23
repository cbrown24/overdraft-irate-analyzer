from flask_restplus import Api
from flask import Blueprint

# from .api 

from .main.controller.irate_controller import api as irate_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Overdraft transaction stats',
          version='1.0',
          description='a flask app with a restplus web service',
          )

api.add_namespace(irate_ns, path='/rates')