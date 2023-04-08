
fixed_size = 1000
def Len(array):
    if isinstance(array, str) == True:
        stringS = ""
        status = True
        i = 0
        while status: 
            stringS += array[i]
            i += 1
            if stringS == array: 
                status = False
        return i   
    else:
        arr = [None for i in range(fixed_size)]
        a = list(array)
        if a == []: 
            return 0
        else: 
            i = 0
            while any(array): 
                arr[i], array[i] = array[i], None
                i+=1      
        return i
arr = [1,2,3,4,5]
print(Len(arr))