class Bike:
    def __init__(self):
        self.type = "Road Bike"
        self.max_gears = 6
        self.gear = 1

    def change_gear(self, increase):
        if increase and self.gear < self.max_gears:
            self.gear += 1
            print("Gear increased to:" , self.gear)

        elif not increase and self.gear > 1:
            self.gear -= 1
            print("Gear decreased to:" , self.gear)

        else:
            print("Gear could not be changed.")

class Cyclist:
    def __init__(self):
        self.name = "Bhavya"
        self.age = 20
        self.weight = 56
        self.proficiency = "Road"
        self.protective_gear = False

    def accelerate(self):
        print("Got to go fast.")

    def apply_brakes(self):
        print("Stopping!")

    def turn(self, direction):
        print("Turning" , direction)

    def wear_protective_gear(self):
        self.protective_gear = True
        print("Protective gear equipped.")