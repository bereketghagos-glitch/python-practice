movies = [
    {"title": "Sheep", "genre": "sci-fi", "rating": 9},
    {"title": "The Man", "genre": "horror", "rating" : 7},
    {"title" : "Fire Fight", "genre" : "action", "rating" : 4}
]
for movie in movies:
    print(movie["title"], movie["rating"])
movies.append({"title": "Freakish", "genre" : "horror", "rating" : 8})
highest = movies[0]
for movie in movies:
     if movie["rating"] > highest["rating"]:
         highest = movie
print(highest["title"], highest["rating"])
lowest = movies[0]
for movie in movies:
    if movie["rating"] < lowest["rating"]:
        lowest = movie
movies.remove(lowest)
print(len(movies))
