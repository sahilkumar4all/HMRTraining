#MOVIE RECOMMENDATION SYSTEM
movie_set = {"ACTION":["Ironman3","Antman","KGF","MI"],
             "Thriller":["KGF","Guardians of galaxy","JUMANJI","THOR"],
             "Comedy":["golmaal","Dhamaal","Antman","golmaal returns"]}

user1 = {"Ironman3","KGF","MI","THOR","Antman"}
user2= {"Ironman3","MI","golmaal"}
#checking common movies between two users
common_movies = user1.intersection(user2)
print(common_movies)
#now we will check that movies of which category , both users love to watch
m = []
action=0
thriller=0
comedy=0

for movie in common_movies:
    if movie in movie_set["ACTION"]:
        action+=1
    if movie in movie_set["Thriller"]:
        thriller+=1
    if movie in movie_set["Comedy"]:
        comedy+=1
        
print(action,thriller,comedy)     


for movie in user1:
    if movie in movie_set["ACTION"]:
        m.append(movie)
print(m)
for movie in m:
    if movie not in user2:
        print("Movies reccomended for you : {}".format(movie))
        







