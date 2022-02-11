# -*- coding: utf-8 -*-
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
par = 0
impar = 0
positivo = 0
negativo = 0
nulo = 0

if num1%2 == 0:
	par = par+1
else:
	impar = impar+1
if num2%2 ==0:
	par = par+1
else:
	impar = impar+1
if num3%2 == 0:
	par = par+1
else:
	impar = impar+1
if num4%2 == 0:
	par = par+1
else:
	impar = impar+1
if num5%2 == 0:
	par = par+1
else:
	impar = impar+1

if num1 > 0:
	positivo = positivo+1
elif num1 == 0:
	nulo = nulo+1
else:
	negativo = negativo +1
if num2 > 0:
	positivo = positivo+1
elif num2 == 0:
	nulo = nulo+1
else:
	negativo = negativo +1
if num3 > 0:
	positivo = positivo+1
elif num3 == 0:
	nulo = nulo+1
else:
	negativo = negativo +1
if num4 > 0:
	positivo = positivo+1
elif num4 == 0:
	nulo = nulo+1
else:
	negativo = negativo +1
if num5 > 0:
	positivo = positivo+1
elif num5 == 0:
	nulo = nulo+1
else:
	negativo = negativo +1

print("%d valor(es) par(es)" % (par))
print("%d valor(es) impar(es)" % (impar))
print("%d valor(es) positivo(s)" % (positivo))
print("%d valor(es) negativo(s)" % (negativo))