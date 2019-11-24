
# Third party libraries
import cv2, time, sys, json
import numpy as np
from datetime import datetime
from darkflow.net.build import TFNet


from src.helper import log
from src import *

from src.controller.ctrl_models import cache, session, running_app
from src.controller import frame_process
        

"""
Start Screen Streaming to predrict content on each frame
Parameters:
- id: Session ID
"""
def run(id):

    log.info('Init - Start loading model.')
    # Tracker: Load model
    tf_net = TFNet({
        'model': MODEL_PATH.format(model=MODEL_NAME),
        'load': WEIGHTS_PATH.format(model=MODEL_NAME),
        'threshold': MODEL_THRESHOLD
    })

    # Camera: Open connection
    log.info('Init - Openning camera connection')
    capture = cv2.VideoCapture(DEVICE_ID)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    file_name = f'test_{id}.txt'


    colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
    i = 0
    while running_app.get():
        start_time = time.time()
        ret, frame = capture.read()
        if ret:
            log.info('Frame processing - Predicting frame')
            results = tf_net.return_predict(frame)

            log.info('Frame processing - Interpretating prediction')
            output = frame_process.run(results, colors, frame, id)   

            # Show frame       
            cv2.imshow('frame', output['frame'])
            
            # Save tracking on log
            res = {
                'time': datetime.now().strftime("%H:%M:%S"),
                'people': output['people']
            }
            with open(f'src/data/tracking_output/{file_name}', "a+") as f:
                f.write(str(res))
                f.write('\n')
        i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
