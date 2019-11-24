# Third party libraries
import cv2


from src.helper import log
from src import *

from src.controller import people_tracking as p

"""
From top-left (x,y) and bottom-right (x,y)
return the centroid point
"""
def calculate_center(x,y,x2,y2):
    return ((x+x2)/2 , (y+y2)/2)

"""
Frame processing
Params:
- results: Tracker prediction
- colors: Random colors vector
- frame: Video frame

Return:
 - frame: Frame to print
 - people: Detected people with its centroids
"""
def run(results, colors, frame, id):
    log.info('New frame output:')
    new_people = {}
    i = 0

    # Track the new detected centroids and related them 
    # with the detected people from the last frame
    for result in results:
        # 1. Get info
        x = result['topleft']['x']
        y = result['topleft']['y']

        x2 = result['bottomright']['x']
        y2 = result['bottomright']['y']

        # 2. Calculate centroid
        centroid = calculate_center(x,y,x2,y2)

        # 3. Add to new frame dictionary
        new_people[i] = {
            'centroid': centroid,
            'x': x,
            'y': y,
            'x2': x2,
            'y2': y2
        }
        i += 1

    results = p.track_new_frame(DEVICE_ID, new_people, id)


    for color, i in zip(colors, results):

            x = results[i]['x']
            y = results[i]['y']

            x2 = results[i]['x2']
            y2 = results[i]['y2']

            centroid = results[i]['centroid']
            tl = (x,y)
            br = (x2,y2)

            confidence = result['confidence']

            # Add info to the frame to print
            text = '{}_{}: {:.0f}%'.format('person', i, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    return {
        'frame': frame,
        'people': new_people
    }