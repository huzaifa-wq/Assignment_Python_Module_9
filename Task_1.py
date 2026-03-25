class Car:
    def __init__(self, registration_number, max_speed ):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

if __name__ == "__main__":
     car = Car("ABC-123", 142)

     print(f"current speed : ",car.current_speed)
     print(f"traveled distance : ",car.traveled_distance)
     print(f"max speed : ",car.max_speed)
     print(f"Registration Numer : ",car.registration_number)