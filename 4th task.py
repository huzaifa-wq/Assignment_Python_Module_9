import random

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
    cars = []

for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))

race_on = True

while race_on:
        for car in cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

            if car.traveled_distance >= 10000:
                race_on = False
                break

print(f"{'Reg No':<10} {'Max Speed':<12} {'Speed':<10} {'Distance':<10}")


for car in cars:
        print(f"{car.registration_number:<10} {car.max_speed:<12} {car.current_speed:<10} {int(car.traveled_distance):<10}")