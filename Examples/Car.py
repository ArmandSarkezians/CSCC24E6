class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __add__(self, other):
        return self.year + other.year

    def __sub__(self, other):
        return self.year - other.year

    def __str__(self):
        return "{} {} {}".format(self.make, self.model, self.year)

    def __eq__(self, other):
        return self.year == other.year


car1 = Car("Volkswagen", "Jetta", 2015)
car2 = Car("Ford", "Fiesta", 2016)
print(car1 + car2)
print(car1 - car2)
print(car1)
