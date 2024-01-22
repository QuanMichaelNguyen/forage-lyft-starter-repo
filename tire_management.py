def check_carrigan_tires(tire_wear_array):
    for wear_value in tire_wear_array:
        if wear_value >= 0.9:
            return True #service needed if any value is 0.9 or more
    return False

def check_octoprime_tires(tire_wear_array):
    sum_value = 0
    for wear_value in tire_wear_array:
        sum_value += wear_value
    if sum_value >= 3:
        return True
    return False
