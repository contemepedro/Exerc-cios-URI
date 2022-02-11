# -*- coding: utf-8 -*-

tempo = int(input())
hora = (tempo//3600)
minuto = ((tempo-3600*hora)//60)
segundo = (tempo-(3600*hora)-(60*minuto))

print("%d:%d:%d" % (hora,minuto,segundo))

exit(0)