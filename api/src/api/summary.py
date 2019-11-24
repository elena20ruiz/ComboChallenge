
from src.helper import response

def get(screen_id):
    # Read file
    with open(f'/src/data/output/test_{screen_id}.txt', 'r') as f:
        lines = f.readlines()

    # Write app

    # Return computed JSON
    response = {}
    return response.make(False, '', response)