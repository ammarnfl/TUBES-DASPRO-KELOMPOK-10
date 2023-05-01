import os
from  Z1_ListFunction import *
from Z2_CSV_Function import *


def load(path : str, filename : str, array : list) -> list: 
    f =  open(os.path.join(path, filename), 'rt')
    arr = ""
    for line in f: 
        arr += line
    f.close()
    array = matriks_csv(array, arr) 
    return array
