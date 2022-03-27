class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car1 = Car("Volkswagen", "Jetta", "2015")
car2 = Car("Ford", "Fiesta", "2016")
print(car1 + car2)
