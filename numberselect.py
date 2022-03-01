def numbersl(selectfgv):
    result = []
    for number in selectfgv:
        if number < 0:
            result.append(number)
            
    return result