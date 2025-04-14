class Car:
    def __init__(self):
        self.make = "Hyundai"
        self.model = "i30 N"
        self.year = 2023

    def display_information(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)

Roadster = Car()
Roadster.display_information()

