chat = True
import webbrowser
Hellointent = ["Hello","Hi","hey","Helloooo"]
while chat:
    val=input("enter value")
    if val in Hellointent:
        print("Hello")
    elif val=="bye" or val=="biee" or val=="byeee":
        print("Bye")
        chat = False
    elif val="open web":
        value = input("enter web address")
        webbrowser.open(value)
        
