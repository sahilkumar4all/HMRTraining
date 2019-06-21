def function1():
    print("function1 inside")
    def function2():
        print("function2 inside")
    return function2
function1()()

