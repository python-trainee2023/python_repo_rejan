class Vehicle:
    def __init__(self, brand, make, color):
        self.brand = brand
        self.make = make
        self.color = color


class Car(Vehicle):
    def __init__(self, brand, make, color, price):
        super().__init__(brand, make, color)
        self.price = price

    def viewCar(self):
        print(f"Brand : {self.brand}")
        print(f"Make: {self.make}")
        print(f"Color: {self.color}")
        print(f"Pricing: {self.price}")


myCar = Car("Ferrari", 2021, "red", "1 million")
myCar.viewCar()

