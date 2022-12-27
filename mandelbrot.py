import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height, width = image.shape

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            c = complex(real, imag)
            color = mandelbrot(c, iters)
            image[y, x] = color

image = np.zeros((500, 500))
create_fractal(-2, 1, -1, 1, image, 20)

plt.imshow(image, cmap='jet')
plt.show()
