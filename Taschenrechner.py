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
    time.sleep(1.5)
    cls()
    operation = input("Please make your selection: +, -, * or /. You can also quit at any time by pressing 'q'  ").lower()
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
            

def currency_converter():
    cls()
    print("Starting currency converter...")
    time.sleep(1.5)
    cls()
    print("Select between these two options: ")
    print("1 = You are living in X and you want to convert money from X to Y.")
    print("2 = You are living in X and you want to convert money from Y to Z.")
   
    
    



def menu():
    print("Welcome to the menu! Do you want to start the calculator or the currency converter? ")
    print("1 = calculator")
    print("2 = currency converter")
    operation = input().lower()
    if(operation == '1' or operation == 'calculator' or operation == 'calc' or operation == 'c' or operation == '1 = calculator'): 
        cls()
        calculator()
    elif(operation == '2' or operation == '2 = currency converter' or operation == 'currency' or operation == 'converter' or operation == 'cc' or operation == 'currency converter'): 
        cls()
        currency_converter()
    elif(operation == 'q'):
            sys.exit(0)
    else:
        cls()
        reboot()


def reboot():
    print("Rebooting...")
    time.sleep(2)
    cls()
    menu()


menu()
