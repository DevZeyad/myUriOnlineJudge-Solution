money = int(input())

print(money)
print(int(money/100) , "nota(s) de R$ 100,00")
money %= 100;
print(int(money/50) , "nota(s) de R$ 50,00")
money %= 50;
print(int(money/20) , "nota(s) de R$ 20,00")
money %= 20;
print(int(money/10) , "nota(s) de R$ 10,00")
money %= 10;
print(int(money/5) , "nota(s) de R$ 5,00")
money %= 5;
print(int(money/2) , "nota(s) de R$ 2,00")
money %= 2;
print(int(money) , "nota(s) de R$ 1,00")
