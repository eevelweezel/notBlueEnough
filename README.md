# notBlueEnough
Because there are times blue isn't blue enough.  Sometimes in 2k+ files. 

This thing batch-updates all images in a directory, replacing all pixels of the of the offending color, adjusting the gradient as needed.  Because marketing.  The quality of the output will depend on the size of the gradient and the relative similarity of the colors you're replacing.

It should preserve transperancy and at least make an effort with GIFs.  Output is saved to a subdirectory named "out."  

dir = input directory

new = hex value (w/o the #) of the replacement color

rep = hex value of the color to be replaced (w/o the #s)

fuzz = size of the gradient, e.g. "100"
