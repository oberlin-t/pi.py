import math
lastx = 0.0
lasty = 5.0
dist = 0
lastx = 0
area = 0

prec = 10000000
for i in range(prec * 5):
    x = i / prec
    y = math.sqrt(25-math.pow(x,2))
    area += (x - lastx) * y
    lastx = x

area += (5 - lastx)

    
pi = (4 * area) / 25
print(pi)


