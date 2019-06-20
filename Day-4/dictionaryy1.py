data = {"roll_no":[1,2,3,4],"name":["ravi","rohit","ram","shyam"]
        }
'''for i in range(len(data["roll_no"])):
    print(data["roll_no"][i],data["name"][i])
'''
#you have to print those names which are starting with "r"

for i in range(len(data["name"])):
    if data["name"][i].startswith('r'):
        print(data["name"][i])
        
