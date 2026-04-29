shows = [ 
    {"title": "Game of Thrones", "genre": "fantasy", "rating": 9},
    {"title": "The Office", "genre": "comedy", "rating": 7},
    {"title": "JJK" , "genre" : "action", "rating" : 8},
    {"title": "The Flash", "genre" : "action", "rating" : 5},
    {"title": "Tokyo Ghoul", "genre" : "psychological", "rating" : 10}

]

for show in shows:
    print(f"{show['title']} - {show['genre']} - {show['rating']}")

highest = shows[0]
for show in shows:
    if show["rating"] > highest["rating"]:
        highest = show
lowest = shows[0]
for show in shows:
    if show["rating"] < lowest["rating"]:
        lowest = show
print(lowest["title"])
print(highest["title"])

average = 0
for show in shows:
    average += show["rating"]
average /= len(shows)
print(average)

shows.append({"title": "Naruto", "genre" : "fantasy", "rating" : 0})

print(len(shows))



