N1,N2,N3,N4 = input().split()

Avg = ((float(N1)*2) + (float(N2)*3) + (float(N3)*4) + (float(N4)*1)) / 10

print("Media:", '%.1f' % Avg)

if Avg >= 7.0:
    print("Aluno aprovado.")
elif Avg < 5.0:
    print("Aluno reprovado.")
elif Avg <= 6.9:
    print("Aluno em exame.")
    newScore = float(input())
    print("Nota do exame:",'%.1f'%newScore)
    newAvg = (newScore + Avg) / 2
    if newAvg >= 5.0:
        print("Aluno aprovado.")
    elif newAvg <= 4.9:
        print("Aluno reprovado.")
    print("Media final:",'%.1f'%newAvg)
