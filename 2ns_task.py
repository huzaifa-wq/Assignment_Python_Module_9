class Car:
    def __init__(self, registration_number, max_speed ):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

if __name__ == "__main__":
    car = Car("ABC-123", 142)

    print(f"current speed : ", car.current_speed)
    print(f"traveled distance : ", car.traveled_distance)
    print(f"max speed : ", car.max_speed)
    print(f"Registration Numer : ", car.registration_number)


    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)

    print(f"current Speed after accelration : ",car.current_speed,"Km/h")

    car.accelerate(-200)
    print("Final speed after emergency brake:", car.current_speed, "km/h")