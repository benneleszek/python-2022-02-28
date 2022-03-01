from pickle import TRUE
from unittest import result


def nagyobb15(szam: int):
    print("Nagyobb-e 15-nél?")
    if szam > 15:
        return True
    else:
        return False

result = nagyobb15(14)
print (result)