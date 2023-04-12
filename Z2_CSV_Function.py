from Z1_ListFunction import * 

def split_csv(line: str) -> list: 
    Appened_Array = [None for i in range(Neff)]
    Appened_Array[0] = Mark
    string = ""
    for i in range(len(line)): 
        if line[i] != ';' and line[i] != '\n': 
            string += line[i]
        else: 
            Appened_Array = Appends(Appened_Array, string)
            string = ""
    if string != "":
        Appened_Array = Appends(Appened_Array, string)
    return Appened_Array


def matriks_csv(arr : list, list_item) -> list: 
    arr[0] = Mark
    for item in list_item: 
        temp = split_csv(item)
        arr = Appends(arr, array_eff_None(temp))
    return arr

## penggunaan split 
    """array = [None for i in range(Neff)]
    array[0] = Mark
    for item in a: 
        temp = split_csv(item)
        array = Appends(array, array_eff_None(temp))"""
    #array = Appends(array, temp)
##debuggingS
"""    array = array_eff_None(array)
    print(array)"""



