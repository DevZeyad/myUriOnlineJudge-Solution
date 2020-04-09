A,B,C = input().split()
if float(A) < float(B):
    tmp = A
    A = B
    B = tmp
if float(A) < float(C):
    tmp = A
    A = C
    C = tmp
if float(B) < float(C):
    tmp = B
    B = C
    C = tmp

if float(A) >= float(B) + float(C):
    print("NAO FORMA TRIANGULO")
elif (float(A)*float(A)) == (float(B)*float(B))+(float(C)*float(C)):
    print("TRIANGULO RETANGULO")
elif (float(A)*float(A)) > (float(B)*float(B))+(float(C)*float(C)):
    print("TRIANGULO OBTUSANGULO")
elif (float(A)*float(A)) < (float(B)*float(B))+(float(C)*float(C)):
    print("TRIANGULO ACUTANGULO")

if float(A) == float(B) == float(C):
    print("TRIANGULO EQUILATERO")
elif float(A) == float(B) or float(A) == float(C) or float(B) == float(C):
    print("TRIANGULO ISOSCELES")
