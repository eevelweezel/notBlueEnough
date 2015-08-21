import sys;
import os;
from PIL import Image;
import itertools;

"""
Batch-process all images in a directory, replacing all pixels of the of the offending color.
Because brands and stuff.
Writes output to a subdirectory named "out."
dir = input directory
new = hex value (w/o the #) of the replacement color
splat args = space-delimited list of hex values to replace (w/o the #s)

"""


def main(null, dir, new, *args):
    rootDir = dir
    print(args)
    if os.path.exists(rootDir+'/out'): 
        pass
    else:
        os.mkdir(rootDir+'/out')
    new = bluify(new)
    old = [bluify(x) for x in args]
    print(old)
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
                            if (r, g, b) in old:
                                pixel[x, y] = new        
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
