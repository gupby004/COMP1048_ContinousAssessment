#Ques1
class Snake:
    def __init__(self):
        self.name = "Ekans"
        self.nickname = "meo"
        self.cry = "*Hiss*"

    def speak(self):
        print(self.cry)

    def coil(self):
        print(self.name, "coils up its own body")

snake = Snake()
snake.speak()

#Ques2
class Cat:
    def __init__(self):
        self.name = "Pat"
        self.nickname = "Billu"
        self.cry = "*Meow*"

    def speak(self):
        print(self.cry)

    def explore(self, location):
        self.location = location
        print("Exploring", self.location)


testcat = Cat()
testcat.speak()

testcat = Cat()
testcat.explore("London")
testcat.explore("New York")


#Ques3
class Sheep:
    def __init__(self):
        self.name = "shaun"
        self.nickname = "shinu"
        self.cry = "*Baaa*"
        self.min_hunger = 0
        self.max_hunger = 100
        self.current_hunger = 50

    def speak(self):
        print(self.cry)

    def eat(self, sustenance):
        if sustenance < 0:
            print("I cannot eat this non-nutritious meal")
        elif sustenance > self.max_hunger:
            print("That is too much food to consume")
        else:
            self.current_hunger -= sustenance
            print ("My current hunger level is:" , self.current_hunger)

testsheep = Sheep()
testsheep.speak()

testsheep = Sheep()
testsheep.eat(120)


#Ques 4
class Mouse:
    def __init__(self):
        self.name = "Miiccee"
        self.nickname = "Danger"
        self.cry = "*Squeek*"
        self.cheese = True

    def speak(self):
        print(self.cry)

    def collect_cheese(self):
        self.cheese = True
        print (self.nickname, "collected a piece of cheese.")

    def deposit_cheese(self):
        self.cheese = False
        print (self.nickname, "stored the cheese.")

testmouse = Mouse()
testmouse.speak()

testmouse = Mouse()
testmouse.collect_cheese()

testmouse = Mouse()
testmouse.deposit_cheese()

#ques 5
class Cow:
    def __init__(self):
        self.name = "Maya"
        self.nickname = "Mimoo"
        self.cry = "*Mooo*"
        self.milk = 0

    def speak(self):
        print(self.cry)

    def produce_milk(self):
        self.milk += 10
        print("I have produced", self.milk , "milk.")

        if self.milk >= 30:
            self.milk_cow()

    def milk_cow(self):
        self.milk = 0
        print("What a relief.")

cow = Cow()
cow.speak()

cow = Cow()
cow.produce_milk()
cow.produce_milk()

cow = Cow()
cow.produce_milk()
cow.produce_milk()
cow.produce_milk()

cow = Cow()
cow.produce_milk()
cow.milk_cow()