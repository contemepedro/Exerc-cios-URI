# -*- coding: utf-8 -*-

tempo = int(input())
ano = (tempo//365)
mes = ((tempo-365*ano)//30) 
dia = ((tempo-365*ano)-(30*mes))

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (ano,mes,dia))

exit(0)