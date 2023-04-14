from Z1_ListFunction import *

def HapusJin(array_of_user : list) -> list: 
    isUsernameExist = False
    username = input("Masukkkan username Jin: ")

    #check username ada atau tidak 
    i = 0 
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][0] == username: 
            role = array_of_user[i][2]
            isUsernameExist = True
            break
        i += 1
    if Marking(array_of_user[i]) == True:
        isUsernameExist = False

    #kondisi jika username ditemukan atau tidak
    if isUsernameExist == True and (role == 'jin_pengumpul' or role == 'jin_pembangun'): 
        choice = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} Y/N? ")
        if choice == 'Y' or choice == 'y': 
            index = get_element_matriks(array_of_user, username)
            array_of_user = Remove(array_of_user, index)
            return array_of_user
        elif choice == 'N' or choice == 'n':
            print("Yah gajadi dihapus")
    else: 
        print("Tidak ada jin dengan username tersebut")

    return array_of_user
