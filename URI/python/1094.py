# -*- coding: utf-8 -*-
n = int(input())
i = 0
totalc = 0
totals = 0
totalr = 0
total = 0
perc = 0
pers = 0
perr = 0

while i<n:
    seq, let = input().split()
    seq, let = int(seq),str(let)
    i = i+1
    if let == 'C':
        totalc = totalc + seq
    if let == 'R':
        totalr = totalr + seq
    if let == 'S':
        totals = totals + seq        
total = totals+totalr+totalc
perc = (totalc*100)/total
perr = (totalr*100)/total
pers = (totals*100)/total
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(totalc))
print("Total de ratos: {}".format(totalr))
print("Total de sapos: {}".format(totals))
print("Percentual de coelhos: {:.2f} %".format(perc))
print("Percentual de ratos: {:.2f} %".format(perr))
print("Percentual de sapos: {:.2f} %".format(pers))