import array as arr

# Lists
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "dates", "papaya", "mango"]

print("Fruits:", fruits)
print("Unpacking fruits:", *fruits)

print(fruits[2])
fruits[2] = "orange"
print("Updated fruits list:", fruits)

comnined_list = letters + fruits + numbers
print("Combined List:", comnined_list)

range_list = list(range(1, 20))
print("Range List:", range_list)

# slicing with step.
print(numbers[1:4:2])  # print index 1 to 3 with step 2.
print(numbers[::2])

# unpacking list
first, *middle, last = fruits
print("First fruit:", first, "Last fruit:", last)
print("Middle fruits:", middle)

fruits.append("kiwi")
print("Fruits after append:", fruits)

fruits.insert(2, "grape")
print("Fruits after insert:", fruits)

fruits.pop()
print("Fruits after pop from end of list:", fruits)

fruits.pop(1)
print("Fruits after pop from index 1:", fruits)

# handle error if item not in the list to remove
try:
    fruits.remove("berry")
    print("Fruits after removing 'berry':", fruits)
except ValueError:
    print("'berry' not found in the list")

print(fruits.count("apple"))

fruits.sort()
print("Sorted fruits:", fruits)

fruits.sort(reverse=True)
print("Sorted fruits descending:", fruits)

# sort complex objects
students = [
    ("Udith", 25),
    ("Nimal", 22),
    ("Kamal", 23),
]


def sort_by_age(student):
    return student[1]


students.sort(key=sort_by_age)
print("Students sorted by age:", students)

# using lambda function. no need of the def sort_by_age function when using lambda expression.
students.sort(key=lambda student: student[0])
print("Students sorted by name:", students)

# lambda functions
# Map function
age_map = map(lambda student: student[1], students)
print(list(age_map))

# Filter function
age_filter = filter(lambda student: student[1] > 22, students)
print(list(age_filter))


# List comprehensions. to use instead of lambda functions like map and filter
student_age = [student[1] for student in students]
print("Student ages using list comprehension:", student_age)

students_above_22 = [student for student in students if student[1] > 22]
print("Students older than 22 using list comprehension:", students_above_22)

# Zip function. merge multiple lists into a list of tuples
names = ["Udith", "Nimal", "Kamal"]
ages = [25, 22, 23]
country = ["Sri Lanka", "India", "Nepal"]
zipped = zip(names, ages, country)
print("Zipped Student details:", list(zipped))


# Arrays. Arrays are similar to lists but can only store elements of the same data type.
# Arrays can be efficient in terms of memory and performance for large datasets. Otherwise lists are preferred in Python due to their versatility.
# need to import array module to use arrays.
numbers_array = arr.array('i', [1, 2, 3, 4, 5])
numbers_array.append(6)
print(numbers_array[5])
