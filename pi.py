import random
import math
total = 0
inSphere = 0
points = input("How many points do you want to compute? > ")

for i in range(int(points)):
    x = random.uniform(0,10)
    y = random.uniform(0,10)
    z = random.uniform(0,10)
    d = math.sqrt(math.pow((x-5), 2) + math.pow((y-5), 2) + math.pow((z-5), 2))
    
    if d <= 5:
        inSphere += 1
        total += 1
    else:
        total += 1

pi = ((inSphere / total) * 1000) / (500/3) 
print("Pi =",pi)

