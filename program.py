x = "pink"
z = 5
y = 3
def firstFunction():
    global z 
    z = 2
    if z > y:
        print("yellow")
    else:
        print("I guess he was wrong", end = " ")
        print(x)

def secondFunction():
    for i in range(3):
        print("red is the color of the day")
        print("blue is the new gold")
        print("purple is the same")
    if z > y:
        print("white")
    else:
        print("orange is the new black")


firstFunction()
secondFunction()



  
    