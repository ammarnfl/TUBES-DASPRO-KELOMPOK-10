from Z1_ListFunction import *

def LaporanJin(array_of_user : list, array_of_material : list): 
    jumlahJin = TotalJin(array_of_user)
    pasir, batu, air = TotalMaterial(array_of_material)
    return jumlahJin, pasir, batu, air


def TotalJin(array_of_user : list) -> int:
    count = 0
    for i in range(Len(array_of_user)): 
        if array_of_user[i][2] == "jin_pembangun" or array_of_user[i][2] == "jin_pengumpul": 
            count += 1
    return count


def TotalMaterial(array_of_material : list) -> str: 
    pasir = array_of_material[1][2]
    batu = array_of_material[2][2]
    air = array_of_material[3][2]

    return pasir, batu, air