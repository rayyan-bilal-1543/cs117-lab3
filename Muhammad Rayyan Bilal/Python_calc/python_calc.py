def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "ERROR! Can't divide by ZERO"
    else:
        return a/b
    
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is EVEN"
    else:
        return f"{num} is ODD"
    
def percentage(part, whole):
    if whole == 0:
        return "ERROR! Can't divide by ZERO"
    else:
        return (part/whole) * 100

while True:  

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Check Even/Odd")
    print("6. Percentage")
    print("7. Exit")


    choice = input("Enter your CHOICE (1-7):")

    if choice == "1":
        a = float(input("Enter FIRST Number:"))
        b = float(input("Enter SECOND Number:"))
        print("Result:", add(a,b))

    elif choice == "2":
        a = float(input("Enter FIRST Number:"))
        b = float(input("Enter SECOND Number:"))
        print("Result:", subtract(a,b))

    elif choice == "3":
        a = float(input("Enter FIRST Number:"))
        b = float(input("Enter SECOND Number:"))
        print("Result:", multiply(a,b))

    elif choice == "4":
        a = float(input("Enter FIRST Number:"))
        b = float(input("Enter SECOND Number:"))
        print("Result:", divide(a,b))

    elif choice == "5":
        num = int(input("Enter a Number:"))
        print(even_odd(num))

    elif choice == "6":
        part = float(input("Enter Part:"))
        whole = float(input("Enter Whole:"))
        print("Result:", percentage(part,whole), "%" )

    elif choice == "7":
        print("Thank you for using!")
        break

    else:
        print("Invalid Choice! Try Again")