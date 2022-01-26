from scipy.optimize import fmin_l_bfgs_b
from math import exp, log
from random import uniform
from neteval import *
from PIL import Image
from pxextract import *
import pickle

def export(xk):
    global counter
    counter += 1
    if counter % 5 == 0:
        endfunc = open("netexp.pkl","wb")
        outlist[1] = list(xk)
        pickle.dump(outlist,endfunc)
        print('dumped')
        endfunc.close()

checks = getpxdata(Image.open("ticks1.jpg"))
exes = getpxdata(Image.open("exes2.jpg"))
dataset = []
for data in checks:
    dataset.append([])
    dataset[-1].append(data)
    dataset[-1].append([1.0])
for data in exes:
    dataset.append([])
    dataset[-1].append(data)
    dataset[-1].append([0.0])

shape = [int(x) for x in input("shape: ").split()]
thetas = []
for x in range(1,len(shape)):
    for y in range(shape[x] * (shape[x-1] + 1)):
        thetas.append(uniform(-1,1))

lambinp = input("lambda (or type 'auto'): ") 
if lambinp == 'auto':
    lamb = abs(sum(getcostderivs(thetas,dataset,shape,0.0)) / (10 * len(thetas))) * len(dataset)
    print("lambda =", lamb)
else:
    lamb = float(lambinp)
    
global counter
outlist = [shape,[]]
counter = 0

minthetas = list(fmin_l_bfgs_b(getcost,thetas,getcostderivs,args=(dataset,shape,lamb),callback=export))
outlist[1] = minthetas

endfunc = open("netexp.pkl","wb")
pickle.dump(outlist,endfunc)
endfunc.close()
