from PIL import Image
import numpy as np
import os

for infile in filelist:
    outfile = os.path.splitest(infile)[0] + ".png"
    if infile != outfile:
        try:
             Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)

pil_im = Image.open('empire.png')
