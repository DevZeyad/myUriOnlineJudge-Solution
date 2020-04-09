values = input().split()
A,B,C,D = values

if int(B) > int(C) and int(D) > int(A) and int(C+D) > int(A+B) and int(C) >= 1 and int(D) >= 1 and int(A) % 2 == 0:
        print("Valores aceitos")
else:
        print("Valores nao aceitos")
