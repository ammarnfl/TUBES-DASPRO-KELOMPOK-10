from F14_Save import *
from Z1_ListFunction import *

def Exit(array_of_user : list, array_of_candi :list , array_of_material : list):
    simpan = input("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah (Y/N)? ")

    while True: 
        if simpan == 'n' or simpan == 'N':
            print("\nKeluar dari program...\n")
            exit()
        elif simpan == 'y' or simpan == 'Y':
            parent = "data"
            folderpath = input("Masukkan nama folder: ")
            folder = parent + "/" + folderpath
            print("\nSaving...\n")
            save(folder, array_of_user, 'user.csv')
            save(folder, array_of_candi, 'candi.csv')
            save(folder, array_of_material, 'bahan_bangunan.csv')
            print(f"Menyimpan folder di {folder}...\n")
            print("Keluar dari program...\n")
            exit()
        print("Input tidak sesuai")
        simpan = input("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah (Y/N)? ")
