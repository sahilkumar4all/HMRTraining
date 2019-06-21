a = 10
b = 0
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
    
addition()
substraction()
multiplication()
division()
