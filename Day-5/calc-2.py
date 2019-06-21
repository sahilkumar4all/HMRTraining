def addition():
    z = a+b
    print(f"addition = {z}")
def substraction():
    z = a-b
    print(f"Substraction = {z}")
def multiplication():
    z = a*b
    print(f"Multiplication = {z}")
def division():
    z = a/b if b!=0 else print("can't be divided by zero")
    print(f"Division = {z}")
print('''
press 1 for addition
press 2 for substraction
press 3 for multiplication
press 4 for division
''')    
a =  int(input("enter first number"))
b= int(input("enter second number"))

ch = input("enter choice")
dict = {"1":addition,
        "2":substraction,
        "3":multiplication,
        "4":division
    }
dict.get(ch)()













