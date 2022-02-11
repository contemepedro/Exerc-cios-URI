# -*- coding: utf-8 -*-

valor = int(input())
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois= 0
um = 0

if valor>=0:
    div100 = valor//100
    cem = cem+div100
    div50 = (valor%100)/50
    cinq = cinq+div50
    div20 = ((valor%100)%50)/20
    vinte = vinte+div20
    div10 = (((valor%100)%50)%20)/10
    dez = dez+div10
    div5 = ((((valor%100)%50)%20)%10)/5
    cinco = cinco+div5
    div2 = (((((valor%100)%50)%20)%10)%5)/2
    dois = dois+div2
    div1 = ((((((valor%100)%50)%20)%10)%5)%2)/1
    um = um+div1
    print(valor)
    print("%d nota(s) de R$ 100,00" % (cem))
    print("%d nota(s) de R$ 50,00" % (cinq))
    print("%d nota(s) de R$ 20,00" % (vinte))
    print("%d nota(s) de R$ 10,00" % (dez))
    print("%d nota(s) de R$ 5,00" % (cinco)) 
    print("%d nota(s) de R$ 2,00" % (dois))
    print("%d nota(s) de R$ 1,00" % (um))