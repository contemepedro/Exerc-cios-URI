# -*- coding: utf-8 -*-

gritos = 0
piscadas = 0

while gritos<3:
    sinais = input()
    if sinais == '---':
        sinais = int(0)
    elif sinais == '--*':
        sinais = int(1)
    elif sinais == '-*-':
        sinais = int(2)
    elif sinais == '-**':
        sinais = int(3)
    elif sinais == '*--':
        sinais = int(4)
    elif sinais == '*-*':
        sinais = int(5)
    elif sinais == '**-':
        sinais = int(6)
    elif sinais == '***':
        sinais = int(7)
    elif sinais == 'caw caw':
        gritos += 1
        print(piscadas)
        piscadas *= 0
    if sinais != 'caw caw':
        piscadas += sinais