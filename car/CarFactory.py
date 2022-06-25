from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from car import Car
from datetime import date
class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine, battery)
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine, battery)
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        current_date = date.today() 
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine, battery)
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
        current_date = date.today()
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        return Car(engine, battery)
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
        current_date = date.today()
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        return Car(engine, battery)

    



