import math
from numpy import *

class julia_fract :
    def __init__(self, const, depth):
        self.c     = const
        self.depth = depth

    def computePoint(self, pt, mode=1):
        n = 0
        if mode == 1:
          z = pt
          c = self.c
        else:
          z = 0.2 - 0.8j
          c = pt
        while n < self.depth:
	   z = z*z + c
           n+=1
	   if z.real*z.real + z.imag*z.imag > 16:
 	       return n
        return n
        
    def computePoint3(self, pt, mode=1):
        n = 0
        if mode == 1:
          z = pt
          c = self.c
        else:
          z = 0
          c = pt
        while n < self.depth:
           z = z*z*z + z*z + c
           n+=1
           if abs(z)>4:
               return n
        return n
        
    def computeJulia(self, size):
      julia = zeros((size[0],size[1]))
      for x in xrange(0, size[0]):
        for y in xrange(0, size[1]):
          z = complex(2*(float(x)/size[0])-1 , 3*(float(y)/size[1])-1.5)
          #print z 
          n = self.computePoint(z,size)
          julia[x,y] = n
      return julia
    
    def computeMandelbrot(self, size):
      mandelbrot = zeros((size[0],size[1]))
      for x in xrange(0, size[0]):
        for y in xrange(0, size[1]):
          z = complex(2*(float(x)/size[0])-1 , 3*(float(y)/size[1])-1.5)
          #print z 
          n = self.computePoint3(z, 0)
          mandelbrot[x,y] = n
      return mandelbrot
      
