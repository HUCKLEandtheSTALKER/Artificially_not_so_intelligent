from PIL import Image

def getpxdata(img):
    out = []
    for x in range(37):
        for y in range(3):
            out.append(imgtopx(img.crop((19*x,19*y,19*(x+1)-1,19*(y+1)-1))))
    return out

def imgtopx(imag):
    ret = []
    for px in list(imag.getdata()):
        ret.append(px[0])
        
    return ret
