
from expiringdict import ExpiringDict


class ExpiringCache():

    def __init__(self):
        self.cache = ExpiringDict(max_len=50, max_age_seconds=300)

    def check_cache(self,key):
        if key in self.cache:
            return self.cache[key]
        else:
            return False

    def add_entry(self, key,value):
        self.cache[key] = value
        return

    def reset(self):
        self.cache = ExpiringDict(max_len=50, max_age_seconds=300)

