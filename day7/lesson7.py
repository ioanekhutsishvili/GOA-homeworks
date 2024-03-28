#hw1
celsius_temp = int(input("please enter temperature in celsius: "))


fahrenheite_temp = (celsius_temp * 1.8) + 32

print(fahrenheite_temp)

#hw2
age = int(input("please enter your age: "))

print(age > 12 and age < 20)
#hw3
length = float(input("enter number: "))
width = float(input("enter number: "))
area = length * width
print(area)
#hw4
user_number = int(input("enter number: "))
print(user_number)

print(user_number > 100 and user_number % 9 )

#hw5 and
print(1 > 100 and 300 < 200)
print(1 > 100 and 50 < 200)
print(1 > 0.5 and 300 < 200)
print(200 > 100 and 100 < 200)
#or
print(1 > 100 or 300 < 200)
print(1 > 100 or 100 < 200)
print(150 > 100 or 300 < 200)
print(150 > 100 or 150 < 200)

