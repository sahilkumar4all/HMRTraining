a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,10):
    print(a+b,end=" ")
    c=a
    a=b
    b=b+c

