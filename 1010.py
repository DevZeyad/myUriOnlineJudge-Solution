product1 = input().split(" ")
product2 = input().split(" ")

code1,nou1,pfou1 = product1
code2,nou2,pfou2 = product2

total = ((int(nou1)*float(pfou1))+(int(nou2)*float(pfou2)))

print("VALOR A PAGAR: R$",'%.2f'%total,end='\n')
