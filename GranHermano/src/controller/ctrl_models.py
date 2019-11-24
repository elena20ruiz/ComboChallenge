from src.models.cache import ExpiringCache
from src.models.running_app import RuningApp
from src.models.session import ControlTime

cache = ExpiringCache()
running_app = RuningApp()
session = ControlTime()