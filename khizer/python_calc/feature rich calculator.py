#calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ERROR! Can't divide by ZERO"
    else:
        return x / y

def even_odd(value):
    if value % 2 == 0:
        return f"{value} is EVEN"
    else:
        return f"{value} is ODD"

def percentage(section, total):
    if total == 0:
        return "ERROR! Can't divide by ZERO"
    else:
        return (section / total) * 100


while True:
    print("A. Addition (+)")
    print("B. Multiplication (×)")
    print("C. Check Even/Odd")
    print("D. Subtraction (-)")
    print("E. Percentage")
    print("F. Division (÷)")
    print("G. Exit")

    choice = input("Enter your CHOICE (A-G): ").upper()

    if choice == "A":
        first = float(input("Enter FIRST number: "))
        second = float(input("Enter SECOND number: "))
        print("Result:", add(first, second))

    elif choice == "B":
        first = float(input("Enter FIRST number: "))
        second = float(input("Enter SECOND number: "))
        print("Result:", multiply(first, second))

    elif choice == "C":
        number = int(input("Enter a number: "))
        print(even_odd(number))

    elif choice == "D":
        first = float(input("Enter FIRST number: "))
        second = float(input("Enter SECOND number: "))
        print("Result:", subtract(first, second))

    elif choice == "E":
        section = float(input("Enter SECTION: "))
        total = float(input("Enter TOTAL: "))
        print("Result:", percentage(section, total), "%")

    elif choice == "F":
        first = float(input("Enter FIRST number: "))
        second = float(input("Enter SECOND number: "))
        print("Result:", divide(first, second))

    elif choice == "G":
        print("BEST OF LUCK FOR FUTURE")
        break

    else:
        print("YOU HAVE CHOSEN AN INVALID INPUT")