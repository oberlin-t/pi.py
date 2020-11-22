a = 0
e = 0
total = 0
inCircle = 0
incFactor = 1

for x in range(20):               
    for x in range(10 * int((1/incFactor))):
        for x in range(10 * int((1/incFactor))):
            a += incFactor            
            d = ((e-5)**2+(a-5)**2)**0.5

            if d <= 5:
               inCircle += 1
               total += 1
            else:
               total += 1
               
        e += incFactor
        a = 0

    incFactor = incFactor/2
    e = 0
    
    pi = ((inCircle / total) * 100) / 25
    print(pi)
