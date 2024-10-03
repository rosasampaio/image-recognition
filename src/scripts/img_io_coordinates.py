import numpy, imageio

def simple_write():
    X,Y = 300,300
    image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)
    image[50, 50, :] = (0xFF, 0xFF, 0xFF)
    imageio.imwrite('output.png', image)


    
if __name__ == '__main__':
    simple_write()