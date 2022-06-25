from abc import ABC
from datetime import date

from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date,current_date):
        # super().__init__(warning_light_is_on)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 2

