import math 
uzunlik=lambda pi,r:2*r*pi
print(uzunlik(math.pi,2 ))
yuza=lambda pi,r:r*pi**2
print(uzunlik(math.pi,10 ))

from math import sqrt
sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))
print(ildizlar)
kvadratlar=list(map(lambda x:x*x,sonlar))
print(kvadratlar)
a=[4,5,6]
b=[7,8,9]
a_plus_b=list(map(lambda x,y:x+y, a,b))
print(a_plus_b)
import random as r
sonlar=r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    return x%2==0
juft_sonlar=list(filter(juftmi,sonlar))
print(juft_sonlar)

