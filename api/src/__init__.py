MODEL_LIST = ['tiny-yolo-voc', 'yolo']
MODEL_DEFAULT = 'tiny-yolo-voc'
MODEL_PATH = 'cfg/{model}.cfg'
WEIGHTS_PATH = 'cfg/{model}.weights'
MODEL_THRESHOLD = 0.35
DEVICE_DEFAULT = 0


__all__ = [
    'MODEL_LIST',
    'MODEL_DEFAULT',
    'MODEL_PATH',
    'WEIGHTS_PATH',
    'MODEL_THRESHOLD',
    'DEVICE_DEFAULT'
]