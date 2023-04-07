def Length(array): 
    if isinstance(array,str) == True :
        array = list(array)
    arrays = []
    i = 0
    status = True
    while status == True :
        arrays += [array[i]]
        i+= 1
        if arrays == array: 
            status = False
    return i