import sys
from src.granhermano import connexion_app
from src import *

if __name__ == '__main__':
    connexion_app.run(host='0.0.0.0', port=8086, threaded=False)


    