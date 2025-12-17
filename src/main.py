# src/main.py

# Importing getsizeof to measure memory size of objects
from sys import getsizeof

print("Hello, Programmer!")

input_name = input("Enter your name: ")
print("Welcome ", input_name)

print(type(input_name))


# getting the number of bytes used by a variable. generator expressions are more memory efficient than list comprehensions.
values = (x * 2 for x in range(10000))  # this is a generator expression
print("\n", type(values))
print("Size of generator object:", getsizeof(
    values))  # size of generator object

values_1 = [x * 2 for x in range(10000)]  # this is a list comprehension
print(type(values_1))
print("Size of list object:", getsizeof(values_1))  # size of list object
