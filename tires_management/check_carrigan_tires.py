from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear


    def needs_service(self):
        for wear_value in self.tire_wear:
            if wear_value >= 0.9:
                return True #service needed if any value is 0.9 or more
        return False


