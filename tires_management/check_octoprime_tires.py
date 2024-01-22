from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        sum_value = 0
        for wear_value in self.tire_wear:
            sum_value += wear_value
        if sum_value >= 3:
            return True
        return False
