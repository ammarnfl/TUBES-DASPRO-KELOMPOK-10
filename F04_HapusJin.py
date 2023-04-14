from Z1_ListFunction import *

def HapusJin(array_of_user : list) -> list: 
    isUsernameExist = False
    username_jin = input("Masukkkan username Jin: ")

    #check username ada atau tidak 
    i = 0 
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][0] == username_jin: 
            role = array_of_user[i][2]
            isUsernameExist = True
            break
        i += 1
    if Marking(array_of_user[i]) == True:
        isUsernameExist = False

    #kondisi jika username ditemukan atau tidak
    if isUsernameExist == True and (role == 'jin_pengumpul' or role == 'jin_pembangun'): 
        choice = input(f"Apakah anda yakin ingin menghapus jin dengan username {username_jin} Y/N? ")
        if choice == 'Y' or choice == 'y': 
            index = get_element_matriks(array_of_user, username_jin)
            array_of_user = Remove(array_of_user, index)
        elif choice == 'N' or choice == 'n':
            print("Yah gajadi dihapus")
    else: 
        print("Tidak ada jin dengan username tersebut")

    return array_of_user, username_jin
