from PIL import Image
import pickle
from neteval import *
from pxextract import *

endfunc = open(input('file: '),"rb")
outlist = pickle.load(endfunc)

testimg = Image.open(input('image file:'))
x = neteval(imgtopx(testimg),inflate(outlist[1],outlist[0]))[-1][1] * 100

if round(x) == 100:
    print("This is a tickmark. I am almost certain.")
elif round(x) == 0:
    print("This is an x. I am almost certain.")
elif x > 50.5:
    print("This is a tickmark. I am",round(x),"percent sure.")
else:
    print("This is a x. I am",round(100-x),"percent sure.")

endfunc.close()
testimg.close()
