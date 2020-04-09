Days = int(input())
ageInYears = int(Days/365)
ageInMonth = int((Days-(ageInYears*365))/30)
ageInDays = int(Days%((ageInYears*365)+(ageInMonth*30)))

print(ageInYears,"ano(s)")
print(ageInMonth,"mes(es)")
print(ageInDays,"dia(s)")
