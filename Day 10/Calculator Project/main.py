from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

#print(operations["*"](4, 8))
calculate = True

print(logo)
n1 = float(input("Please type your first number: "))
while calculate:
    o = input(" +\n -\n *\n /\n Which operator would you like to use?: ")

    n2 = float(input("Please type your second number: "))

    n3 = operations[o](n1, n2)

    print(n3)
    n1 = n3

    again = input("Do you want to continue working working with the previous calculation?"
              "type 'y' for yes, type 'n' for no.")

    if again == "y":
        n1 = n3
    else:
        n3 = 0