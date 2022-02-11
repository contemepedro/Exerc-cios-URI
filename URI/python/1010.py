# -*- coding: utf-8 -*-

cod1, n1, valor1 = input().split()
cod1, n1, valor1 = int(cod1), int(n1), float(valor1)
cod2, n2, valor2 = input().split()
cod2, n2, valor2 = int(cod2), int(n2), float(valor2)
pagar = ((valor1*n1)+(valor2*n2))

print("VALOR A PAGAR: R$ %.2f" % (pagar))

exit(0)