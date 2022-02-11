# -*- coding: utf-8 -*-

p = int(input())
while p > 0:
    p = p-1
    l = []
    m = int(input())
    while m > 0:
        m = m-1
        l.append(input())
    main = l[0]
    for m in l:
        if m != main:
            main = 'ingles'
            break
    print(main)