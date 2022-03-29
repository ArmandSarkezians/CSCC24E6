class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "{} {} {}".format(self.make, self.model, self.year)


car1 = Car("Ford", "Fiesta", 2016)
print(car1)
