sellerName = input()
fixedSalary = float(input())
salesMadeInMonth = float(input())
totalSalary = fixedSalary + (salesMadeInMonth * (15/100))

print("TOTAL = R$",'%.2f'%totalSalary,end='\n')
