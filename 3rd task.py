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

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours


if __name__ == "__main__":
    car = Car("ABC-123", 142)

    car.accelerate(60)
    car.drive(1.5 )

    print("Current speed:", car.current_speed, "km/h")
    print("Travelled distance:", car.traveled_distance, "km")