from neteval import *
import pickle
from pxextract import *
from PIL import Image

endfunc = open("netexp.pkl","rb")
outlist = pickle.load(endfunc)

checks = getpxdata(Image.open("ticks1.jpg"))

for x in checks:
    print(neteval(x,inflate(outlist[1],outlist[0]))[-1][1])

testimg = Image.open('testimg.jpg')
print(' ')
print(neteval(testimg.getdata(),inflate(outlist[1],outlist[0]))[-1][1])

endfunc.close()
