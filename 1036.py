A,B,C = input().split()
root = (float(B)*float(B)) - (4*float(A)*float(C))
div = 2 * float(A)

if div == 0.0 or root < 0.0:
    print("Impossivel calcular")
else:
    R1 = (- float(B) + (pow(root, 0.5))) / div
    R2 = (- float(B) - (pow(root, 0.5))) / div
    print("R1 =",'%.5f'%R1)
    print("R2 =",'%.5f'%R2)
