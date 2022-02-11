# -*- coding: utf-8 -*-

N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)
Media = (N1*2+N2*3+N3*4+N4*1)/10

if Media>=7:
    print("Media: %.1f" % (Media))
    print("Aluno aprovado.")

elif Media<5:
    print("Media: %.1f" % (Media))
    print("Aluno reprovado.")

else:
    N5 = float(input())
    Mediaf = (Media+N5)/2
    if Mediaf >= 5:
        print("Media: %.1f" % (Media))
        print("Aluno em exame.")
        print("Nota do exame: %.1f" % (N5))
        print("Aluno aprovado.")
        print("Media final: %.1f" % (Mediaf))
    else:
        print("Media: %.1f" % (Media))
        print("Aluno em exame.")
        print("Nota do exame: %.1f" % (N5))
        print("Aluno reprovado.")
        print("Media final: %.1f" % (Mediaf))
    
exit(0)