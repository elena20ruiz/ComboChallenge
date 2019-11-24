from datetime import datetime


class ControlTime():

    def __init__(self):
        self.people = {}

    def update_value(self, key, value):
        self.people[key] = value
    
    def check_value(self, key):
        if key in self.people:
            return True
        return False

    def get_value(self, key):
        return self.people[key]

    def get_all_keys(self):
        return len(self.people)

    def remove_key(self, key):
        del self.people[key]

    def print(self):
        print(f'New status at {datetime.now().strftime("%H:%M:%S")}')
        for p in self.people:
            print(f'Person {p}: Time on room {self.people[p][0]}. Last update: {self.people[p][1].strftime("%H:%M:%S")}')


CT = ControlTime()