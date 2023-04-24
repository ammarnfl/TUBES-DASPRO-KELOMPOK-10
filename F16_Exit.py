from F14_Save import *
from Z1_ListFunction import *

def exit(array_of_candi : list, array_of_user : list, array_of_material: list):
    while login_status == True:
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        folder_input = input("Masukkan nama folder: ")
        username = input("Masukkan username jin: ")
        if simpan == 'n' or simpan == 'N':
            exit
        elif simpan == 'y' or simpan == 'Y':
            save(folder_input, 'user.csv', username)
        else:
            simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    return exit        

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