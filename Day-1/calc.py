a=int(input("enter first number"))
b=int(input("enter second number"))
print('''enter choice 1.add
                      2.subtract
                      3.divide
                      4.multiply''')
c=int(input("enter choice"))
if c==1:
	print(a+b)
elif c==2:
	print(a-b)
elif c==3:
	print(a/b)
elif c==4:
	print(a*b)
else:print("wrong choice")
