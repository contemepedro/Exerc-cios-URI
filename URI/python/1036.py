# -*- coding: utf-8 -*-

from math import sqrt

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
delta=(b**2)-(4*a*c)

if a==0 :
    print("Impossivel calcular")

elif delta<0 :
    print("Impossivel calcular")
    
else :
    delta = sqrt(delta)
    x1=(-b+delta)/(2*a)
    x2=(-b-delta)/(2*a)
    print ("R1 = %.5f\nR2 = %.5f" % (x1,x2))
    
exit(0)