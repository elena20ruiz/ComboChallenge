
from src.helper import response, log

import cv2
import time
import numpy as np

from darkflow.net.build import TFNet

def start():
    log.info('Start capturing the people')
    
    tf_net = TFNet({
        'model': MODEL_PATH.format(model=model_name),
        'load': WEIGHTS_PATH.format(model=model_name),
        'threshold': MODEL_THRESHOLD
    })
    return response.make(False, response={0: 'hello'})