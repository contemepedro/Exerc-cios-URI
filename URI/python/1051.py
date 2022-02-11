# -*- coding: utf-8 -*-

salario = float(input())
imp1 = ((salario-2000)*0.08)
imp2 = ((((salario-2000)-1000)*0.18)+(1000*0.08))
imp3 = ((((salario-2000)-2500)*0.28)+(1000*0.08)+(1500*0.18))

if salario <= 2000:
	print("Isento")
elif salario > 2000 and salario <= 3000:
	print("R$ %.2f" % (imp1))
elif salario > 3000 and salario <= 4500:
	print("R$ %.2f" % (imp2))
else:
	print("R$ %.2f" % (imp3))

exit(0)