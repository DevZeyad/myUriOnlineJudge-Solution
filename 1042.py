a,b,c = input().split()
if int(a) < int(b) and int(a) < int(c):
    mini = a
    if int(b) < int(c):
        mid = b
        maxi = c
    else:
        mid = c
        maxi = b
elif int(b) < int(a) and int(b) < int(c):
    mini = b
    if int(a) < int (c):
        mid = a
        maxi = c
    else:
        mid = c
        maxi = a
else:
    mini = c
    if int(a) < int(b):
        mid = a
        maxi = b
    else:
        mid = b
        maxi = a
print(mini)
print(mid)
print(maxi)
print()
print(a)
print(b)
print(c)
