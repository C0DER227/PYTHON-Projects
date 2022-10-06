def add(a, b):
    answer = a + b
    print(str(a) + " + " + str( b) + " = " + str(answer) + "\n")
def Sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b ) + " = " + str(answer) + "\n")
def Mul(a, b):
    answer = a*b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def Div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        Sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        Mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division" )
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        Div(a, b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()