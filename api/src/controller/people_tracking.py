from src.helper import log
from datetime import datetime
from src.controller.ctrl_cache import cache
from src.controller.ctrl_session import CT

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  


def redistribute_people(lpeople, new_people):
    return

def track_new_frame(cam_id, new_people):
    log.debug('Comparing two following frames ... ')

    # Check if exists last frame
    res = cache.check_cache(f'cam_{cam_id}')
    if res:
        lpeople = res
        # HERE HAS TO BE THE TRACKER CALCULATION BUT NO TIME...
        result = new_people
    else:
        result = new_people
    cache.add_entry(f'cam_{cam_id}', result)

    time_log = []
    actual_time =  datetime.now()

    for p in new_people:
        if not CT.check_value(p):
            t = [0 ,actual_time]
            CT.update_value(p, t)
        else:
            value = CT.get_value(p)
            last_diff = (actual_time - value[1]).total_seconds()
            t = [value[0] + last_diff, actual_time]
            CT.update_value(p, t)

    ini = len(new_people)
    fi = CT.get_all_keys()
    for p in range(ini,fi):
        v = CT.get_value(p)
        diff_sec = (actual_time - v[1]).total_seconds()
        if diff_sec >= 3:
            CT.remove_key(p)
    
    CT.print()
    return result