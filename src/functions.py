def greet(first_name, last_name):
    print(f"Hello, Welcome {first_name} {last_name}")


def farewell(first_name):
    print(f"Goodbye, See you later {first_name}")


print("Greeting")
greet("Udith", "Nalaka")
print("Farewell")
farewell("Udith")


def greet_message(name):
    return f"Hello, {name}!"


message = greet_message("Udith")
print(message)

# write to a file
with open("greeting.txt", "w") as file:
    file.write(message)


# optinal parameter
def increment(number, by=1):
    return number + by


print(increment(3))
print(increment(5, 2))


# variable number of arguments
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num

    return total


print("Multiply two numbers 2 x 3 =", multiply(2, 3))
print("Multiply three numbers 2 x 3 x 4 =", multiply(2, 3, 4))

# xxargs (passing object as key value pairs)


def save_user(**user_info):
    print("User info:", user_info)
    first_name = user_info["first_name"]
    last_name = user_info["last_name"]
    age = user_info["age"]
    print(f"Hello, {first_name} {last_name}")
    print(f"Age: {age}")


save_user(first_name="Udith", last_name="Nalaka", age=45)
