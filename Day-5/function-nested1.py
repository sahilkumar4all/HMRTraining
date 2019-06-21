a = int(input("enter first number"))
b  =int(input("enter second number"))
def calc():
    def addition():
        z = a+b
        print("sum is",z)
        
    def substraction():
        z = a-b
        print("sub is",z)
        
    def multiplication():
        z = a*b
        print("multiplication",z)
        
    def division():
        z = a/b
        
    return addition,substraction,multiplication,division
val = calc()
print(val)
#calc()[0]()
