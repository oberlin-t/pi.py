import math
lastx = 0.0
lasty = 5.0
dist = 0

prec = 3000000
for i in range(prec * 5):
    x = i / prec
    y = math.sqrt(25-math.pow(x,2))
    dist += math.sqrt(math.pow((x-lastx),2) + math.pow((y-lasty),2))
    lastx = x
    lasty = y

dist += math.sqrt(math.pow((5-lastx),2) + math.pow((0-lasty),2))
    
pi = (dist * 4) / 10
print(pi)
