import random

def get_car_data():
    data = {
        "rpm": random.randint(700, 3000),
        "coolant_temp": random.randint(150, 220),
        "throttle": random.randint(0, 100),
        "battery": round(random.uniform(12.0, 14.5), 1),
        "speed": random.randint(0, 70)
    }

    return data


