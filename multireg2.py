def regress(points,alpha,thetas):
    stop = False
    while not stop:
        derivs = getderivs(thetas,points)
        cost1 = cost(thetas,points)
        print(cost1,derivs,thetas)
        for x in range(len(derivs)):
            thetas[x] -= derivs[x] * alpha
        if max(derivs) < 0.001 and min(derivs) > -0.001:
            stop = True
    return derivs,thetas
        
def getderivs(thetas,points):
    derivs = [0] * len(thetas)
    m = len(points)
    for point in points:
        err = error(thetas,point)
        derivs[0] += err
        for x in range(len(thetas)-1):
            derivs[x+1] += err * point[x]
            
    for x in range(len(derivs)):
        derivs[x] /= len(points)
   
    return derivs

def cost(thetas,points):
    m = len(points)
    totcost = 0
    for point in points:
        err = error(thetas,point)
        totcost += err*err/2/m
    return totcost

def error(thetas,point):
    retval = 0 
    retval += thetas[0]
    for x in range(len(point)-1):
        retval += point[x] * thetas[x+1]
    return retval - point[-1]

f = open(input('file name: '),'r')
points = []
for line in f:
    temp = []
    for item in line.split():
        temp.append(float(item))
    points.append(temp)

lines = []
for x in range(len(points[0])-1):
    lines.append([])
for point in points:
    for x in range(len(point)-1):
        lines[x].append(point[x])

rngs = []
avgs = []
for line in lines:
    rngs.append(max(line) - min(line))
    avgs.append(sum(line) / len(line))

for point in points:
    for x in range(len(point)-1):
        point[x] = (point[x] - avgs[x]) / rngs[x]
    
print(regress(tuple(points),float(input('alpha: ')),[0]*len(points[1])))
