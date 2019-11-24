

from flask import jsonify, request
import os
import subprocess
import threading, time
from multiprocessing import Process

# Global variables
from src.helper import response, log
from src.controller import screen

THREADS = []

def start():
    log.info('Start capturing the people')
    try:
        process = Process(target=screen.run)
        process.start()
        log.info(process)
        THREADS.append(process)
        return response.make(False, response={0: 'Running'})
    
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

