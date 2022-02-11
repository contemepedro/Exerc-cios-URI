# -*- coding: utf-8 -*-

num1, num2, num3 = input().split()
num1, num2, num3 = int(num1),int(num2),int(num3)

if num1>=num2 and num1>=num3 and num2>=num3: 
	print("%d\n%d\n%d\n" % (num3,num2,num1))
	print("%d\n%d\n%d" % (num1,num2,num3))
elif num1>=num2 and num1>=num3 and num3>=num2:
	print("%d\n%d\n%d\n" % (num2,num3,num1))
	print("%d\n%d\n%d" % (num1,num2,num3))
elif num2>=num1 and num2>=num3 and num1>=num3:
	print("%d\n%d\n%d\n" % (num3,num1,num2))
	print("%d\n%d\n%d" % (num1,num2,num3))
elif num2>=num1 and num2>=num3 and num3>=num1:
	print("%d\n%d\n%d\n" % (num1,num3,num2))
	print("%d\n%d\n%d" % (num1,num2,num3))
elif num3>=num1 and num3>=num2 and num1>=num2:
	print("%d\n%d\n%d\n" % (num2,num1,num3))
	print("%d\n%d\n%d" % (num1,num2,num3))
elif num3>=num1 and num3>=num2 and num2>=num1:
	print("%d\n%d\n%d\n" % (num1,num2,num3))
	print("%d\n%d\n%d" % (num1,num2,num3))

exit(0)