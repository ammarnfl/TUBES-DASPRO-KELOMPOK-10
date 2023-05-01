from Z1_ListFunction import * 


def split_csv(line: str) -> list: 
    Appened_Array = [None for i in range(Neff)]
    Appened_Array[0] = Mark
    string = ""
    for i in range(len(line)): 
        if line[i] != ';' and line[i] != '\n' and line[i] !='': 
            string += line[i]
        else: 
            Appened_Array = Appends(Appened_Array, string)
            string = ""
    if string != "":
        Appened_Array = Appends(Appened_Array, string)
    return Appened_Array


def matriks_csv(arr : list, line : str) -> list: 
    arr[0] = Mark
    temp = ""
    for i in range(len(line)): 
        temp += line[i]
        if line[i] == '\n': 
            temp_array = split_csv(temp)
            arr = Appends(arr, array_eff_None(temp_array))
            temp = ""
    return arr

