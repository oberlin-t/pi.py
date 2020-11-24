import random
total = 0
inCircle = 0
points = input("How many points do you want to compute? > ")

for i in range(int(points)):
    x = random.uniform(0,10)
    y = random.uniform(0,10)
    d = ((x-5)**2+(y-5)**2)**0.5

    if d <= 5:
        inCircle += 1
        total += 1
    else:
        total += 1

pi = ((inCircle / total) * 100) / 25 
print("Pi =",pi)

