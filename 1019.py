timeSeconds = int(input())
hours = int(timeSeconds / 3600)
minutes = int(int((timeSeconds/60))%60)
seconds = int(timeSeconds%60)

print(hours,end=':')
print(minutes,end=':')
print(seconds)
