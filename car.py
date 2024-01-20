from abc import ABC, abstractmethod

class Engine:
    def needs_service(self):
        pass
class CapuletEngine(Engine):
    def __init__(self) -> None:
        super().__init__()
        self.last_service_mileage = None
        self.current_mileage = None
    def needs_service(self):
        return super().needs_service()
    
class WilloughbyEngine(Engine):
    def __init__(self) -> None:
        super().__init__()
        self.last_service_mileage = None
        self.current_mileage = None
    def needs_service(self):
        return super().needs_service()

class StermanEngine(Engine):
    def __init__(self) -> None:
        super().__init__()
        self.last_service_mileage = None
        self.current_mileage = None
    def needs_service(self):
        return super().needs_service()

class Battery:
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def __init__(self) -> None:
        super().__init__()
        self.last_service_date = None
        self.current_date = None
    def needs_service(self):
        return super().needs_service()

class NubbinBattery(Battery):
    def __init__(self) -> None:
        super().__init__()
        self.last_service_date = None
        self.current_date = None
    def needs_service(self):
        return super().needs_service()
    

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = Engine()
        self.battery = Battery()
    @abstractmethod
    def needs_service(self):
        pass

class CarFactory(Car):
    def create_calliope(self):
        self.current_date = None
        self.last_service_date = None
        self.current_mileage = None
        self.last_service_mileage = None

    def create_glissade(self):
        self.current_date = None
        self.last_service_date = None
        self.current_mileage = None
        self.last_service_mileage = None
    
    def palindrome(self):
        self.current_date = None
        self.last_service_date = None
        self.warning_light_on =  False

    def create_rorschach(self):
        self.current_date = None
        self.last_service_date = None
        self.current_mileage = None
        self.last_service_mileage = None
    
    def create_thovex(self):
        self.current_date = None
        self.last_service_date = None
        self.current_mileage = None
        self.last_service_mileage = None