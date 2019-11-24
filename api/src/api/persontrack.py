

from flask import jsonify, request
import os
import subprocess
import threading
import time
from multiprocessing import Process

# Global variables
from src.helper import response, log
from src.controller import screen

THREADS = []


def start():
    log.info('Start capturing the people')
    try:
        # Number of lists
        list = os.listdir(os.getcwd() +'/src/data/output/') 
        number_files = len(list)
        process = Process(target=screen.run, args=(number_files+1,))
        process.start()
        THREADS.append(process)
        return response.make(False, response={'screen_id': number_files+1})

    except Exception as e:
        log.error('ERROR while recording')
        log.error(e)
        return response.make(True, message=str(e))

def stop():
    log.info('Start capturing the people')
    try:
        THREADS[0].stop()
        return response.make(False, response={0: 'Closed'})
    
    except Exception as e:
        log.error('ERROR while recording')
        log.error(e)
        return response.make(True, message=str(e))

