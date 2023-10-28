class Car:
    total_cars = 0
    car_brand = "Unknown"
    def __init__(self, color, speed, model):
        self.speed = speed
        self.color = color
        self.model = model
        Car.total_cars += 1
        def strat(self):
            print(f"The {self.color} {self.model} car has started")
        def stop(self):
            print(f"The {self.color} {self.model} car has stopped")
    def accelerate(self, increase_speed):
        self.speed += increase_speed
        print(f"The {self.color} {self.model} car has accelerated to {self.speed} km/h.")
        def decelerate(self, decrease_speed):
        self.speed -= decrease_speed
        print(f"The {self.color} {self.model} car has decelerated to {self.speed} km/h.")
def change_color(self, new_color):
    self.color = new_color
    car1 = Car("White", 110, "Audi")
    car2 = Car("Yellow", 150, "Shkoda")
    car1.start()
    car2.start()
    car1.accelerate(20)
    car2.accelerate(30)
    car1.decelerate(10)
    car2.decelerate(15)
    car1.stop()
    car2.stop()
    car1.change_color("Red")
    car2.change_color("Black")
    print(f"Общее количество авто: {Car.total_cars}")
    print(f"Бренд авто: {Car.car_brand}")