import sys;
import os;
from PIL import Image;


"""
Batch-update images in a directory, replacing all pixels of the of the offending color and an adjustable gradient.
Because marketing.  It does preserve transperancy, but doesn't do so well with .GIFs.  Yet.
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
            im = Image.open(rootDir+'/'+fname) 
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
                            if r in range(old[0]-n,old[0]+n) and g in range(old[1]-n,old[1]+n) and b in range(old[2]-n,old[2]+n):
                                offset = (r-old[0],g-old[1],b-old[2])
                                pixel[x,y] = (new[0]-offset[0],new[1]-offset[1],new[2]-offset[2],a)
                        except TypeError:
                            print('Some kinda type weirdness: '+fname)                              
            im.save(rootDir+'/out/'+fname) 
    return
    
    
def bluify(thing):
    a = int(thing[:2], 16)
    b = int(thing[2:4], 16)
    c = int(thing[4:6], 16)
    return (a, b, c)
    
    
if __name__ == '__main__':
    main(*sys.argv)
