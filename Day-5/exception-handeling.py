#exception Handeling
try:
    a  = 11
    b = 0
    c = a/b
    print(c)
except BaseException as ex:
    print(ex)
finally:
    print("this is finally block")
