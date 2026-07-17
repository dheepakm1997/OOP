class Train:
    cars = 5
    car_capacity = 10

    def print_cars(self):
        print(f"Number of cars: {self.cars}")

    def total_capacity(self):
        print(f"Total capacity: {self.cars * self.car_capacity}")


train_1 = Train()

train_1.print_cars()
train_1.total_capacity()