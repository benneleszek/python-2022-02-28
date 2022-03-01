
from itertools import count
import numbers

from pyparsing import nums

def lista (numbersfgv):
    count = 0
    for number in numbersfgv:
        if number < 0:
            count+=1
    return count

#nums =  [1,-5,1,13,-7,9,11,21,-33,44,55,11,22,30,11]

#print(lista(nums))
