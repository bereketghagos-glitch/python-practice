claudy = {
    "name": "Jacob",
    "age": 17,
    "grades": [9, 4, 5, 12, 3]
}

print(claudy["name"])
print(claudy["age"])

claudy["grades"].append(18)
claudy["grades"].remove(min(claudy["grades"]))

for grade in claudy["grades"]:
    print(grade)

print(len(claudy["grades"]))