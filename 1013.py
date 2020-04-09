inputs = input().split(" ")
a,b,c = inputs
maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
result = (int(maior) + int(c) + abs(int(maior) - int(c))) / 2

print('%d'%result , "eh o maior")
