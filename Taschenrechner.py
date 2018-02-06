import os
import sys
import time

#creates command to clear the shell
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#adds num1 and num2 together
def add(num1, num2):
    print(num1 + num2)

#subtracts num1 and num2 
def sub(num1, num2):
    print(num1 - num2)

#multiplies num1 and num2
def mul(num1, num2):
    print(num1 * num2)

#divides num1 and num2
def div(num1, num2):
    print(num1 / num2)

        
def calculator():
    print("Starting calculator...")
    time.sleep(1)
    print("Please make your selection: +, -, * or /. You can also quit at any time by pressing 'q'  ")
    operation = input()
    if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != 'q'):
        cls()
        print("Please enter a valid selection")
        reboot()
    elif(operation == 'q'):
        sys.exit(0)
    else:
        print("You picked " +operation)
        time.sleep(1)
        cls()
        try:
            Num1 = float(input("Please type in your first number:   "))
            Num2 = float(input("Please type in your second number:  "))
        except ValueError:
            cls()
            print("Please enter a valid selection")
            reboot()

        if(operation == '+'):
            add(Num1, Num2)
        elif(operation == '-'):
            sub(Num1, Num2)
        elif(operation == '*'):
            mul(Num1, Num2)
        elif(operation == '/'):
            div(Num1, Num2)
        elif(operation == 'q'):
            sys.exit(0)
            

def menu():
    print("Welcome to the menu! Do you want to start the calculator or the currency converter? ")
    print("1 = calculator")
    print("2 = currency converter")
    operation = input()
    if(operation == '1'):
        time.sleep(0.1)
        cls()
        calculator()
    elif(operation == '2'):
        time.sleep(0.1)
        cls()
        print("There is no currency converter")
    else:
        time.sleep(0.1)
        cls()
        print("Please enter a valid number")


def reboot():
    print("Do you want to reboot? Yes | No")
    operation = input().lower
    if(operation == 'yes', 'y', '1'):
        cls()
        menu()
    else:
        time.sleep(1)




menu()