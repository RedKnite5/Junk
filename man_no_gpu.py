#   python man_no_gpu.py
from numba import autojit
import numpy as np
from pylab import imshow, show
from timeit import default_timer as timer
from PIL import Image
from PIL import ImageTk
import tkinter as tk

@autojit
def mandel(x, y, max_iters):
  """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
  """
  
  c = complex(x, y)
  z = 0.0j
  for i in range(max_iters):
    z = z*z + c
    if (z.real*z.real + z.imag*z.imag) >= 4:
      return i

  return max_iters

@autojit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
  height = image.shape[0]
  width = image.shape[1]

  pixel_size_x = (max_x - min_x) / width
  pixel_size_y = (max_y - min_y) / height
    
  for x in range(width):
    real = min_x + x * pixel_size_x
    for y in range(height):
      imag = min_y + y * pixel_size_y
      color = mandel(real, imag, iters)
      image[y, x] = color


image = np.zeros((1024, 1536), dtype = np.uint8)
start = timer()
create_fractal(-2.0, 1.0, -1.0, 1.0, image, 30) 
dt = timer() - start

print("Mandelbrot created in %f s" % dt)
imshow(image)
show()

'''
root = tk.Tk()
canvas = tk.Canvas(root,width = 600, height = 600)
canvas.pack()

im=Image.frombytes('L', (image.shape[1],image.shape[0]), image.astype('b').tostring())
photo = ImageTk.PhotoImage(image=im)

canvas.create_image(0,0,image=photo)

root.mainloop()
'''




