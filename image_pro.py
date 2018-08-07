import mod
import pylab
import mahotas as mh
import numpy
# python image_pro.py


dna = mh.imread("dna.jpeg")
pylab.imshow(dna.squeeze())
pylab.gray()
print(dna.shape)
print(dna.dtype)
print(dna.max())
print(dna.min())
dna = dna.squeeze()
dnaf = mh.gaussian_filter(dna, 8)
dnag = (dnaf).astype('uint8')
T = mh.thresholding.otsu(dnag)
pylab.imshow(dnag > T)
pylab.show()