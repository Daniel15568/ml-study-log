# set up & hello world
print("Hello world")

# drawing a shape
print("   /|")
print("  / |")
print(" /  |")
print("/   |")

# variables & data types
character_name = "John"
character_age = "35"
isMale = True
print("There once a man named " + character_name + ",")
print("He was " + character_age + " years old.")
character_name2 = "Tom"
print("He really liked the name " + character_name2 + ",")
print("but didn't like being " + character_age + ".")

# working with String
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(phrase[0])
print(phrase.index("a"))
print(phrase.replace("Giraffe","Elephant"))

# working with Numbers
from math import *
print(-2.0987)
print(3 * 4.5)
print(10 % 3)
my_num = 5
print(str(my_num) + " is my favorite number.")
num = -10
print(abs(num))
print("10^2: " + str(pow(num,2)))
print(max(5,1,10,100))
print(min(4,2,6,0))
print("Round: " + str(round(3.7)))
print("Floor of 3.7: " + str(floor(3.7)))
print("Ceil of 3.7: " + str(ceil(3.7)))
print("sqrt of 36: " + str(sqrt(36)))

# Getting input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "!")
print("You are " + age + ".")

# Building a basic caculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)

# Mad Libs Game
color = input("Enter the color: ")
plural_nouns = input("Enter plural nouns: ")
celebrity = input("Enter celebrity: ")
print(f"Roses are {color}")
print(f"{plural_nouns} are blue")
print(f"I love {celebrity}")

# Lists & List Functions
lucky_numbers = [4, 8, 10, 32, 55]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
print(friends[1:3]) # [inclusive : exclusive]
friends[1] = "Mike"
print(friends[1:])
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1,"Holy")
print(friends)
friends.remove("Oscar")
print(friends)
friends.pop()
print(friends)

friends_list = ["Kevin", "Jim", "Josh", "Irene", "Jim"]
print(friends_list.count("Jim"))
friends_list.sort()
print(friends_list)
lucky_numbers.reverse()
print(lucky_numbers)

# Tuples
coordinates = [(4,5), (6,7), (8,10)]
print(coordinates)

Functions
def say_hi(name, age):
    print("Hello " + name + "Your age is " + age + ".")

say_hi("Mike", "44")

# Return Statement
def cube(num):
    return num*num*num

print(cube(3))

# if statements & comparision
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(4,2,10))

# Dictionaries
month_conversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(month_conversions.get("Luv", "Not a valid key"))

# for loop
friends = ["Jim","Kevin","Irene"]
for friend in friends:
    print(friend)

for index in range(3,10): # inclusive ~ exclusive
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

# 2D list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(number_grid[0][2])

for row in number_grid:
    for col in row:
        print(col)

# Try/Except
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as Err:
    print(Err)
except ValueError:
    print("Value error")

# Reading/ Write files
employee_file = open('employees.txt',"a")
employee_file.write("\nToby - Salesman")

employee_file.close()

# class
from Student import Student
student1 = Student("Jim","Business",3.5, False)
print(student1.on_honor_role())
