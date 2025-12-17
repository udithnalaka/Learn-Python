# fizz_biss exercise

def fizz_biss(input_number):
    if input_number % 3 == 0 and input_number % 5 == 0:
        return "FizzBiss"
    elif input_number % 3 == 0:
        return "Fizz"
    elif input_number % 5 == 0:
        return "Biss"
    else:
        return input_number


print(fizz_biss(15))  # FizzBiss
print(fizz_biss(9))   # Fizz
print(fizz_biss(10))  # Biss
print(fizz_biss(7))   # 7
