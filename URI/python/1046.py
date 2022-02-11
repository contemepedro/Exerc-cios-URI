# -*- coding: utf-8 -*-

inicio, fim = input().split()
inicio, fim = int(inicio), int(fim)

if fim > inicio: 
	print("O JOGO DUROU %d HORA(S)" % (fim-inicio))
else:
	print("O JOGO DUROU %d HORA(S)" % ((fim+24)-inicio))

exit(0)