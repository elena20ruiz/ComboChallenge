
from src.helper import response


def get(screen_id):
    # Read file
    with open(f'/src/data/output/test_{screen_id}.txt', 'r') as f:
        lines = f.readlines()
    # Return computed JSON
    return response.make(False, '', response)