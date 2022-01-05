from scipy.optimize import fmin_bfgs
from math import exp, log

f = open(input('file name: '),'r')
points = []
for line in f:
    points.append([])
    for piece in line.split():
        points[-1].append(float(piece))
    
def cost(thetas,points):
    cost = 0
    for point in points:
        cost += point[-1] * log(h0(thetas,point[:-1])) + (1 - point[-1]) * log(1 - h0(thetas,point[:-1]))
    cost /= (-1 * len(points))
    return cost
    
def h0(thetas,xs):
    thetat = thetas[0]
    for x in range(len(xs)):
        thetat += xs[x] * thetas[x+1]
    retval = 1.0 / (1 + exp(thetat * -1))
    if retval == 1:
        retval = 0.999
    elif retval == 0:
        retval = 0.001
    return retval

def correct(params,points):
    right = 0
    wrong = 0
    for point in points:
        if abs(h0(params,point[:-1]) - point[-1]) < 0.5:
            right += 1
        else:
            wrong += 1
    print('right: ', right, ', wrong: ', wrong)

thetas = [0,0,0]

params = fmin_bfgs(cost,thetas,args=(points,))
correct(params,points)
