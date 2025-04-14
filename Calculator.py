class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a-b
    def multiply(self,a , b):
        return a*b
    def divide(self, a ,b):
        return a/b

cal = Calculator()
print(cal.add(1,5))
print(cal.subtract(40,5))
print(cal.multiply(1,8))
print(cal.divide(5,4))