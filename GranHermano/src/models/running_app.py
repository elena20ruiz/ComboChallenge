class RuningApp():
    def __init__(self):
        self.running = True
    def start(self):
        self.running = True
    def stop(self):
        self.running = False
    def get(self):
        return self.running
