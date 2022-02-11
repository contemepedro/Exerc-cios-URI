# -*- coding: utf-8 -*-

d1, d2, d3 = input().split()
d1, d2, d3 = int(d1), int(d2), int(d3)

#1
if d1>d2 and d2<=d3:
    print(':)')
#2
elif d1<d2 and d2>=d3:
    print(':(')
#3
elif d1<d2 and d2<d3 and (d2-d1)>(d3-d2):
    print(':(')
#4 
elif d1<d2 and d2<d3 and (d2-d1)<=(d3-d2):
    print(':)')
#5
elif d1>d2 and d2>d3 and (d1-d2)>(d2-d3):
    print(':)')
#6
elif d1>d2 and d2>d3 and (d1-d2)<=(d2-d3):
    print(':(')
#7
elif d1==d2 and d2<d3:
    print(':)')
#8
elif d1==d2 and d2>d3:
    print(':(')
else:
    print(':(')