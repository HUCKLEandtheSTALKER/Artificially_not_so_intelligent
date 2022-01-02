def regress(points,alpha,m=0,b=0):
    stop = False
    while not stop:
        derivs = getcostderivatives(m,b,points)
        m -= derivs[0] * alpha
        b -= derivs[1] * alpha
        if abs(derivs[0]) < 0.01 and abs(derivs[1]) < 0.01:
            stop = True
            return(m,b)
    
def getcostderivatives(m,b,points):
    valm = 0
    valb = 0
    for pair in points:
        valm += error(m,b,pair[0],pair[1]) * pair[0]
        valb += error(m,b,pair[0],pair[1])
    valm /= len(points)
    valb /= len(points)
    
    return (valm,valb)
    
def error(m,b,x,y):
    return m*x + b - y


f = open(input('file name: '),'r')
points = []
for line in f:
    temp = line.split()
    points.append((float(temp[0]),float(temp[1])))

print(regress(points,float(input('alpha: '))))
