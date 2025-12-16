
today_temp = 9

if today_temp > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif today_temp < 10:
    print("It's a cold day")
else:
    print("It's nice day")

print("Enjoy your day!")

# ternary operator
age = 24
message = "You are eligible to vote." if age >= 18 else "You are not eligible to vote."
print(message)

### OR/ AND /NOT operators in if conditions ###
high_income = True
good_credit = True
is_student = False
if high_income and good_credit and not is_student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if age >= 18 and age < 65:
    print("You have to keep working")

# same s above using chained comparison
if 18 <= age < 65:
    print("You have to keep working")
