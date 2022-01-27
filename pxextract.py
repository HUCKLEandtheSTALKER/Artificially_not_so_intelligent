from PIL import Image

def getpxdata(img):
    out = []
    for x in range(37):
        for y in range(3):
            out.append(imgtopx(img.crop((19*x,19*y,19*(x+1)-1,19*(y+1)-1))))
    return out

def imgtopx(imag):
    ret = []
    if imag.format == "PNG":
        for px in list(imag.getdata()):
            ret.append(255-px[3])
        return ret
    else:
        l = list(imag.getdata())
        if type(l[0]) == type((1,2)):
            for px in l:
                ret.append(px[0])
            return ret
        else:
            return l
