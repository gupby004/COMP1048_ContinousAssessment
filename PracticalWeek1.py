#Practical
#Ques1
def square(a):
    return (a ** 2)
a = 3
b = 5
result = square(a)
result2 = square(b)
print(a, "squared is" , result)
print(b, "squared is" , result2)


#Ques2
def odd_even(number):
    if number % 2 == 0:
        print(number , "is an even number")
    else:
        print(number, "is an odd number")

odd_even(1)
odd_even(4)

#Ques3
def avg(number):
    sum = 0
    for value in number:
        sum += value
    print("Average is" , sum / len(number))

avg([1,2,3,4,5])
avg([17,34,63,45,5])