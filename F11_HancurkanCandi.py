from Z1_ListFunction import *

def HancurkanCandi(array_of_candi : list, id_candi : str) -> str:
    isUsernameExist = False

    #check id ada atau tidak
    i = 0
    while Marking(array_of_candi[i]) == False:
        if array_of_candi[i][0] == id_candi:
            isUsernameExist = True
            break
        i += 1
    
    #kondisi jika id ditemukan
    if isUsernameExist == True:
        choice = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)?")
        if choice == 'Y' or choice == 'y':
            index = get_element_matriks(array_of_candi, id_candi)
            array_to_None(array_of_candi, index)
            print("Candi telah berhasil dihancurkan.")
        elif choice == 'N' or choice == 'n':
            print("Yah gajadi dihancurin.")
    else:
        print("Tidak ada candi dengan ID tersebut.")

    return array_of_candi