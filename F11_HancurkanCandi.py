from Z1_ListFunction import *

def HancurkanCandi(array_of_candi : list, id_candi : str) -> str:
    isIDexist = False
    #check id ada atau tidak
    i = 0
    while Marking(array_of_candi[i]) == False:
        if array_of_candi[i][0] == id_candi:
            isIDexist = True
            break
        i += 1

    if isIDexist == True: 
        choice = input(f"\nApakah anda yakin ingin menghancurkan candi dengan nomor ID {id_candi} (Y/N)? ")
        while True:
            if choice == 'Y' or choice == 'y': 
                array_of_candi[int(id_candi)] = ['', Mark]
                print(f"Candi dengan nomor ID {id_candi} berhasil dihancurkan!\n")
                break
            elif choice == 'N' or choice == 'n': 
                print(f"Candi dengan id {id_candi} tidak jadi dihancurkan")
                break
            print("\nInput tidak valid")
            choice = input(f"\nApakah anda yakin ingin menghancurkan candi dengan nomor ID {id_candi} (Y/N)?")
    else: 
        print("Tidak ada candi dengan ID tersebut\n")
    
    #kondisi jika id ditemukan
    return array_of_candi