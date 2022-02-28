szulev = input("Add meg a születési éved:")
if int(szulev) > 2022:
    print('Jövőbeli dátumot adtál meg, nem megfelelő dátum!')
elif int(szulev) >=2010:
    print('Ebben az évtizedben születtél')
else:
    print('Nem ebben az évtizedben születtél')
