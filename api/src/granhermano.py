# Third party
import connexion
from flask_cors import CORS
import os

from src.helper import log
from src import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
connexion_app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
flask_app = connexion_app.app
flask_app.config['JSON_AS_ASCII'] = False
connexion_app.add_api('openapi.yaml', arguments={'title': 'GranHermano API'})
CORS(flask_app)

@flask_app.route('/')
def alive_check():
    return 'Welcome to GranHermano API!', 200

