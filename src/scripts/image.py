import OpenImageIO as oiio
import numpy as np

def simple_write():
    filename = "simple.tif"
    xres = 320
    yres = 240
    channels = 3  # RGB
    pixels = np.zeros((yres, xres, channels), dtype=np.uint8)

    out = oiio.ImageOutput.create(filename)
    if out:
        spec = oiio.ImageSpec(xres, yres, channels, 'uint8')
        out.open(filename, spec)
        out.write_image(pixels)
        out.close()
       
        
if __name__ == '__main__':
    simple_write()