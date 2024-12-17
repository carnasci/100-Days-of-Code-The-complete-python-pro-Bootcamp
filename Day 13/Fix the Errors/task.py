try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please type in a numerical value like 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
