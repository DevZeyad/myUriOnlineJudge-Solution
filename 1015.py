first = input().split(" ")
second = input().split(" ")

x1,y1 = first
x2,y2 = second

form1 = pow((float(x2)-float(x1)),2)
form2 = pow((float(y2)-float(y1)),2)
distance = pow((form1+form2),0.5)

print('%.4f'%distance)
