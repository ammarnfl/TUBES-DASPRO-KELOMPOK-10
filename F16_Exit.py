from F14_Save import *
from Z1_ListFunction import *

def Exit(array_of_user : list, array_of_candi :list , array_of_material : list):
    simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if simpan == 'n' or simpan == 'N':
        exit()
    elif simpan == 'y' or simpan == 'Y':
        parent = "data"
        folderpath = input("Masukkan nama folder: ")
        folder = parent + "/" + folderpath

        save(folder, array_of_user, 'user.csv')
        save(folder, array_of_candi, 'candi.csv')
        save(folder, array_of_material, 'bahan_bangunan.csv')
        
    exit()