import os
import sys
import time 

def cls(,,,,):
    os.system('cls' if os.name=='nt' else 'clear') #creates command to clear the shell

def add(num1, num2):
    print(num1 + num2) #adds num1 and num2 together

def sub(num1, num2):
    print(num1 - num2) #subtracts num1 and num2 

def mul(num1, num2):
    print(num1 * num2) #multiplies num1 and num2

def div(num1, num2):
    print(num1 / num2) #divides num1 and num2

def calculator():
    print("Starting calculator...")
    time.sleep(1)
    print("Please make your selection: +, -, * or /. You can also quit at any time by pressing 'q'  ")
    operation = input()
    if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != 'q'):
        print("Please enter a valid selection")
    elif(operation == 'q'):
        sys.exit(0)
    else:
        print("You picked " +operation)
        time.sleep(1)
        cls()
        Num1 = float(input("Please type in your first number:   ")) 
        Num2 = float(input("Please type in your second number:  ")) #converting the string values into float
        if(operation == '+'):
            add(Num1, Num2)
        if(operation == '-'):
            sub(Num1, Num2)
        if(operation == '*'):
            mul(Num1, Num2)
        if(operation == '/'):
            div(Num1, Num2)
        if(operation == 'q'):
            sys.exit(0)


calculator()
calculator()