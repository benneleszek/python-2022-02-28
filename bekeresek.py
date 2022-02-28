def bekeres_nev():
    neve = input('Adja meg a nevét:')
    return neve

def bekeres_szulev():
    szulev = input('Adja meg a születési évét:')
    return szulev


nev = "unknown"
while nev != "":
    nev = bekeres_nev()
    print(nev)
    if nev != "":
        print(bekeres_szulev())
