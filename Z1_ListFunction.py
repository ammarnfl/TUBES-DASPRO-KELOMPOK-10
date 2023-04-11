Neff = 105
Mark = -9999
arr = [None for i in range(Neff)]
arr[0] = Mark

#--------------------------------------------------#
#Fungsi untuk marking
def Marking(string : str) -> bool:
    return str(string) == str(Mark) 

#Fungsi untuk appends ke array
def Appends(array: list, b: str, i: int = 0) -> list: 
    while True:
        if Marking(array[i]) == True:
            array[i+1], array[i] = Mark, b
            return array
        elif array[i] == None: 
            array[i] = b
            return array
        i += 1

#Fungsi untuk menghitung Len dari array
def Len(array : list, i: int = 0) -> int: 
    while True: 
        if Marking(array[i]): 
            return i
        i += 1

def Len_None(array : list, i: int = 0) -> int: 
    while True: 
        if array[i] == None: 
            return i
        i += 1

def array_eff(list : list, i : int = 0) -> list: 
    arr = [0 for i in range(Len(list))]
    while list[i] != Mark: 
        arr[i] = list[i]
        i += 1
    return arr

def array_eff_None(list : list, i : int = 0) -> list: 
    arr = [0 for i in range(Len_None(list))]
    while list[i] != None: 
        arr[i] = list[i]
        i += 1
    return arr
#contoh Implementasi 
""" for item in array: 
    arr = Appends(arr, item)
    print(arr)
    """