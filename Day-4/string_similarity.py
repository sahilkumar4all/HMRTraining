#to find how 2 sentence is similar
string1 = "hi"
string2 = "hello"

token1 = string1.split()
token2 = string2.split()

set1 = set(token1)
set2 = set(token2)

data_union = set1.union(set2)
data_intersection = set1.intersection(set2)
#Jaccards INDEX
similar  =  len(data_intersection)/len(data_union)
print("String similarity = {}%".format(similar*100))


