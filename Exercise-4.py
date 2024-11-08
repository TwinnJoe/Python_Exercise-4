# Question 1: Using a for loop with a list

fruits = ["Apple","Banana","Orange","Pear"]

for fruit in fruits:
    print(fruit)

# Question 2: Using a while loop for countdown

count = 5
while count > 0:
    print(count)
    count -= 1

# Question 3: Using a for loop with range()

for i in range(1,11):
    print(i**2)

# Question 4: Using the random module
import random

colors = ["Red","Green","Yellow","Blue","Purple","Nude"]


for color in colors:

    random_colors = random.sample(colors, 3)
    print(random_colors)


# Question 5: Creating and using a custom module
import math_operations

print(math_operations.add(2,20))
print(math_operations.divide(2,20))
print(math_operations.multiply(2,20))
print(math_operations.subtract(2,20))




