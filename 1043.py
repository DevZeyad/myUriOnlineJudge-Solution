A,B,C = input().split()
if (float(A) < float(B)+float(C)) and (float(B) < float(A)+float(C)) and (float(C) < float(B)+float(A)):
    Perimetro = float(A) + float(B) + float(C)
    print("Perimetro =",'%.1f'%Perimetro)
else:
    Area = 0.5 * (float(A)+float(B)) * float(C)
    print("Area =",'%.1f'%Area)
