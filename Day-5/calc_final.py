def calc(operator):
    z = eval(x+operator+y)
    print(z)
print('''
Press 1 for addition
press 2 for substraction
press 3 for multiplication
press 4 for division''')
x = input("enter first no")
y = input("enter  second no")
choice  = input("enter operation you wanna perform")
dict = {"1":"+",
        "2":"-",
        "3":"*",
        "4":"/"}
opr = dict.get(choice)
calc(opr)
