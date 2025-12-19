
numbers = [1, 2, 3, 4, 5]
try:
    print(numbers[5])
except IndexError as ie:
    print("Index out of range error:", ie)


try:
    # no need to close the file explicitly when using 'with' statement
    with open("greeting.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:", content)

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print("Welcome ", name, "you are", age, "years old")

    age_div = 100 / age
    print("You have lived for", age * 365, "days approximately.")

except (ValueError, ZeroDivisionError) as e:
    print("Invalid input for age. Please enter a number greater than zero. Exception: ", e)
finally:
    print("Thank you for using the program.")

print("Program continues...")


# raise an exception from a function


def calculate_born_year(age):
    if age <= 0:
        raise ValueError("Age must be greater than zero.")
    return 2025 - age


try:
    born_year = calculate_born_year(-1)
    print("You were born in:", born_year)
except ValueError as error:
    print(error)
