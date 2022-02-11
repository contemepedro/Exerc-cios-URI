# -*- coding: utf-8 -*-

while True:
  try:
    num,num2 = map(int,input().split())
    cont = num - 1
    cont2 = num2 -1
    if num ==0:
      num = 1
    if num2 == 0:
      num2 = 1
    
    while cont > 0:
      num = num * cont
      
      cont -= 1
    while cont2 >0:
      num2 = num2 * cont2
      cont2 -=1
    print(num+num2)
  except:
    break