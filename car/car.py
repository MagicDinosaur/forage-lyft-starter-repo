class Car:
    def __init__(self,Battery,Engine):
        self.engine = Engine
        self.battery = Battery
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
