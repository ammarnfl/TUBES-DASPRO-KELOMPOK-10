
from Z1_ListFunction import *

def ubah_jin(array_of_user : list) -> list:
    isUsernameExist = False
    username = input("Masukkkan username Jin: ")
    #check username ada atau tidak 
    i = 0 
    while array_of_user[i] != Mark: 
        if array_of_user[i][0] == username: 
            role = array_of_user[i][2]
            isUsernameExist = True
            break
        i += 1
    if array_of_user[i] == Mark:
        isUsernameExist = False

    #kondisi jika username ditemukan atau tidak
    tipe = ""
    tipe_opposite = ""
    #kondisi jika username ada atau tidak
    if isUsernameExist == True: 
        if role == "jin_pembangun": 
            tipe = "Pembangun"
            tipe_opposite = "Pengumpul"
        elif role == "jin_pengumpul": 
            tipe = "Pengumpul"
            tipe_opposite = "Pembangun"
        #menentukan tipe jin diubah atau tidak
        choice = input(f'\nJin ini bertipe "{tipe}". Apakah yakin ingin mengubah ke tipe "{tipe_opposite}" (Y/N)?\n')
        #mengubah role dari jin_pembangun ke jin_pengumpul
        if choice == 'Y' or choice == 'y' and tipe == "Pembangun" and role != "": 
            role = "jin_pengumpul"
            print(f'\nBerhasil ubah jin {username} ke tipe "{tipe_opposite}"\n')
        elif choice == 'N' or choice == 'y': 
            print("Yah, gagal ubah jin")
        #mengubah role dari jin_pengumpul ke jin_pengumpul
        if choice == 'Y'or choice == 'y' and tipe == "Pengumpul" and role != "":
            role = "jin_pembangun"
            print(f'\nBerhasil ubah jin {username} ke tipe "{tipe_opposite}"\n')
        elif choice == 'N' or choice == 'y': 
            print("Yah, gagal ubah jin")
        array_of_user [i][2] = role
    else: 
        print(f'\nTidak ada jin dengan username "{username}"\n')
    return array_of_user
