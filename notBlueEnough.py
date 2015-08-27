import sys;
import os;
from PIL import Image;

"""
Batch-update images in a directory, replacing all pixels of the of the offending color and an adjustable gradient.
Because marketing.  It preserves transperancy and does ...ok... withh GIFs.
Writes output to a subdirectory named "out."

dir = input directory
new = hex value (w/o the #) of the replacement color
rep = hex value of the color to be replaced (w/o the #s)
fuzz = size of the gradient.

"""

def main(null, dir, new, rep, fuzz):
    rootDir = dir
    n = int(fuzz)
    if os.path.exists(rootDir+'/out'): 
        pass
    else:
        os.mkdir(rootDir+'/out')
    new = bluify(new)
    old = bluify(rep)
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            try:
                im = Image.open(rootDir+'/'+fname) 
            except IOError:
                print(fname + ' has issues.')   
            im = im.convert('RGBA')
            pixel = im.load()
            width, height = im.size
            for x in range(width):
                for y in range(height):
                    if type(pixel[x,y]) != int:  
                        try:                    
                            if len(pixel[x,y]) == 3:
                                r,g,b = pixel[x,y]
                            else: 
                                r,g,b,a = pixel[x,y]
                            off = offset(old,n)         
                            if r in range(off[0][0],off[0][1]) and g in range(off[1][0],off[1][1]) and b in range(off[2][0],off[2][1]):
                                diff = (r-old[0],g-old[1],b-old[2])
                                pixel[x,y] = (new[0]-diff[0],new[1]-diff[1],new[2]-diff[2],a)
                        except TypeError:
                            print('Some kinda type weirdness: '+fname)        
                           
            im.save(rootDir+'/out/'+fname) 
    return
    
    
def bluify(thing):
    a = int(thing[:2], 16)
    b = int(thing[2:4], 16)
    c = int(thing[4:6], 16)
    return (a, b, c)

#TODO: check the math here...       
def offset(nold, fuzz):
    out = []
    for i in nold:
        a = i - fuzz
        b = i + fuzz
        if a < 0:
            a = 0
        elif a > 255:
            a = 255
        else:
            pass
        if b < 0:
            b = 0
        elif b > 255:
            b = 255
        else:
            pass
        tmp = []
        tmp.append(a)
        tmp.append(b)        
        out.append(tmp)            
    return (out)
    
if __name__ == '__main__':
    main(*sys.argv)
