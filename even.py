#Írj egy programot ami bekér egy számot
#True-t ír ki, ha a szám páros, amúgy false-t

szam = input('Írj be egy számot:')
print(int(szam) % 2 == 0)

szam = input('Írj be egy számot:')
if int(szam) % 2 == 0:
    print("Páros")

else:
    print("Páratlan")