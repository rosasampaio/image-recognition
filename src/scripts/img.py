import imageio.v3 as iio

def simple_write():
    im = iio.imread('imageio:astronaut.png')
    im.shape  # im is a numpy array
    (512, 512, 3)
    iio.imwrite('astronaut-gray.jpg', im[:, :, 0])
    
    
if __name__ == '__main__':
    simple_write()