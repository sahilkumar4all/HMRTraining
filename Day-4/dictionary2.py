data = [{"id":1,"name":"ravi","marks":[99,98,97]},
        {"id":2,"name":"Shyam","marks":[58,85,97]},
        {"id":3,"name":"ramu","marks":[90,50,74]},
        {"id":4,"name":"john","marks":[10,5,20]},
        {"id":5,"name":"suresh","marks":[2,5,25]}]
#1. calculate average of marks of each students 
#2.  print id , name along with average of students's marks
avg = []
a = 0

for i in range(len(data)):
    
    a = sum(data[i]["marks"])
    a = a//len(data[0]["marks"])
    print(data[i]["name"],"=>",a)
    avg.append(a)
print(avg)
for i in range(len(avg)):
    if(avg[i]>90):
        print(avg[i],"A")
    elif avg[i]>60 and avg[i]<90:
        print(avg[i],"B")
    elif avg[i]>40 and avg[i]<60:
        print(avg[i],"C")
    else:print(avg[i],"F")

for i in range(len(data)):
    data[i]["average"] = avg[i]

print(data)






