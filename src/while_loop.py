
number = 100
while number > 0:
    print("Current Number:", number)
    number //= 2


command = ""
while command.lower() != "exit":
    command = input(">>: ")
    print("Echo:", command)


# print even numbers from 0 to 10 and count the total even numbers
count = 0
num = 10
while num > 0:
    if num % 2 == 0:
        print(num)
        count += 1
    num -= 1
print("Total even numbers:", count)
