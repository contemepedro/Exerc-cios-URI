# -*- coding: utf-8 -*-

valor = float(input())
valorn = int(valor)
valorm = int( 100*valor - 100*int(valor))
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
cent1 = 0
cent5 = 0
cent10 = 0
cent25 = 0
cent50 = 0
real = 0

if valor>=0.00:
    div100 = valorn//100
    cem = cem+div100
    div50 = (valorn%100)//50
    cinq = cinq+div50
    div20 = ((valorn%100)%50)//20
    vinte = vinte+div20
    div10 = (((valorn%100)%50)%20)//10
    dez = dez+div10
    div5 = ((((valorn%100)%50)%20)%10)//5
    cinco = cinco+div5
    div2 = (((((valorn%100)%50)%20)%10)%5)//2
    dois = dois+div2
    div1 = ((((((valorn%100)%50)%20)%10)%5)%2)
    real = real+div1
    div05 = valorm//50
    cent50 = cent50+div05
    div025 = ((valorm)%50)//25
    cent25 = cent25+div025
    div010 = ((valorm%50)%25)//10
    cent10 = cent10+div010
    div005 = (((valorm%50)%25)%10)//5
    cent5 = cent5+div005
    div001 = ((((valorm%50)%20)%10)%5)
    cent1 = cent1+div001
    print("NOTAS:")
    print("%d nota(s) de R$ 100.00" % (cem))
    print("%d nota(s) de R$ 50.00" % (cinq))
    print("%d nota(s) de R$ 20.00" % (vinte))
    print("%d nota(s) de R$ 10.00" % (dez))
    print("%d nota(s) de R$ 5.00" % (cinco)) 
    print("%d nota(s) de R$ 2.00" % (dois))
    print("MOEDAS:")
    print("%d moeda(s) de R$ 1.00" % (real))
    print("%d moeda(s) de R$ 0.50" % (cent50))
    print("%d moeda(s) de R$ 0.25" % (cent25))
    print("%d moeda(s) de R$ 0.10" % (cent10))
    print("%d moeda(s) de R$ 0.05" % (cent5))
    print("%d moeda(s) de R$ 0.01" % (cent1))

exit(0)