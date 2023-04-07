#pengganti fungsi append()
def appends(array, a): 
    newarr = [0 for i in range(len(array) + 1)]
    for i in range(lengthI(newarr)): 
        if i != len(newarr) - 1:
            newarr[i] = array[i]
        else: 
            newarr[i] = a
    return newarr

#pengganti fungsi pop()
def pops(array, a): 
    newarr = []
    for i in range(lengthI(array)): 
        if i != a: 
            newarr = appends(newarr, array[i])
    return newarr

#pengganti fungsi len()
def Length(array): 
    if isinstance(array,str) :
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
# length untuk Integer
def lengthI(array): 
    arrays = []
    status = True
    i = 0
    while status == True: 
        arrays = appends(arrays, array[i])
        i += 1
        if arrays == array: 
            status = False
    return i

# length untuk Array
def lengthS(string): 
    stringS = ""
    status = True
    i = 0
    while status: 
        stringS += string[i]
        i += 1
        if stringS == string: 
            status = False
    return i

#pengganti fungsi sort 
def sorts(array): 
    for i in range(lengthI(array)): 
        for j in range(0, lengthI(array)-i-1): 
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j]
    return array

#pengganti fungsi split()
def splits(arr, b): 
    newarr = []
    bruh = newarr
    a = ""
    for i in range(lengthS(arr)): 
        if arr[i] == b: 
            newarr = appends(newarr, a)
            a = ""
        else: 
            a += arr[i]
    newarr = appends(newarr, a)
    if bruh == newarr:
        return newarr
    else: 
        return arr


arr = "Daspro"
print(Length(arr))
