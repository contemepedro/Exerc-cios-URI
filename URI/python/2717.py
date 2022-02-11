# -*- coding: utf-8 -*-

tfalta = int(input()) 
tpres1, tpres2 = input().split()
tpres1, tpres2 = int(tpres1), int(tpres2)

if tpres1 + tpres2 <= tfalta:
	print("Farei hoje!")
else:
	print("Deixa para amanha!")

exit(0)