from neteval import *
import pickle
from pxextract import *
from PIL import Image

def sign(x):
    return int(x/(2 * abs(x)) + 0.5)

endfunc = open("netexp.pkl","rb")
outlist = pickle.load(endfunc)

checks = getpxdata(Image.open("MIX.jpg"))

right = 0
wrong = 0

for x in checks:
    guess = sign(round(neteval(x,inflate(outlist[1],outlist[0]))[-1][1]*100)-50.5)
    ans = (checks.index(x) // 3) % 2
    print(guess,ans)
    if guess == ans:
        right += 1
    else:
        wrong += 1

print('')
print('right:',right,'wrong:',wrong)

testimg = Image.open('testimg.jpg')
print(' ')
print(neteval(testimg.getdata(),inflate(outlist[1],outlist[0]))[-1][1])

endfunc.close()
