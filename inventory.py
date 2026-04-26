invent = [
    {"name" : "shampoo", "price": 6, "quantity": 12},
    {"name": "toothpaste", "price" : 3, "quantity": 20},
    {"name" : "sanitizer", "price": 4, "quantity" : 8}
]
for item in invent:
    print(item["name"], item["price"])
invent.append({"name": "soap", "price" : 2, "quantity" : 15})
lowest = invent[0]  
for item in invent:
    if item["price"] < lowest["price"]:
        lowest = item
print(lowest["name"], lowest["price"])
print(len(invent))
    
