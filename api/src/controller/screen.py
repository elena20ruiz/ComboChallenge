

import cv2
import time
import numpy as np
import sys
import json
from datetime import datetime
from darkflow.net.build import TFNet


from src.helper import log
from src import *


def calculate_center(x,y,x2,y2):
    return ((x+x2)/2 , (y+y2)/2)

def track_results(results, colors, frame):
    people = []
    log.info('New frame: ----------------')
    for color, result in zip(colors, results):
        if result['label'] == 'person':

            x = result['topleft']['x']
            y = result['topleft']['y']

            x2 = result['bottomright']['x']
            y2 = result['bottomright']['y']

            tl = (x,y)
            br = (x2,y2)
            
            (centerx , centery) = calculate_center(x,y,x2,y2)
            people.append({
                'cx': centerx,
                'cy': centery
            })
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format('person', confidence * 100)
            log.info(f'person {centerx}, {centery}')
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    return {
        'frame': frame,
        'people': people
    }
        


def run(id):
    # VIDEO CONNECTION --------------
    log.info('Start loading model ...')
    # Load model
    tf_net = TFNet({
        'model': MODEL_PATH.format(model=MODEL_NAME),
        'load': WEIGHTS_PATH.format(model=MODEL_NAME),
        'threshold': MODEL_THRESHOLD
    })
    # Open camera connection
    log.info('Open the camera device ...')
    capture = cv2.VideoCapture(DEVICE_ID)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    file_name = f'test_{id}.txt'

    colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
    i = 0
    while True:
        start_time = time.time()
        ret, frame = capture.read()
        if ret:
            results = tf_net.return_predict(frame)
            output = track_results(results, colors, frame)   

            # Show frame        
            cv2.imshow('frame', output['frame'])
            print('FPS {:.1f}'.format(1 / (time.time() - start_time)))
            
            # Save tracking
            res = {
                'time': datetime.now().strftime("%H:%M:%S"),
                'people': output['people']
            }
            with open(f'src/data/output/{file_name}', "a+") as f:
                f.write(str(res))
                f.write('\n')
            time.sleep(WAIT_TIME)
        i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
