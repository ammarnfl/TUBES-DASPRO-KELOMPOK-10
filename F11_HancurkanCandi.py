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
        choice = input(f"Apakah anda yakin ingin menghancurkan\n candi ID: {id_candi} (Y/N) ")
        if choice == 'Y' or choice == 'y': 
            array_of_candi[int(id_candi)] = ['', Mark]
    else: 
        print("Tidak ada candi dengan ID tersebut")
    
    #kondisi jika id ditemukan
    

    return array_of_candi