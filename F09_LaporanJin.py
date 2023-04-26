from Z1_ListFunction import *

def LaporanJin(array_of_user : list, array_of_material : list, array_of_candi : list) -> str: 
    jumlahJin, jumlahJinPembangun, jumlahJinPengumpul, = TotalJin(array_of_user)
    pasir, batu, air = TotalMaterial(array_of_material)
    jinMalas, JinRajin = JinTerajinArray(array_of_user, array_of_candi)
    return jumlahJin, jumlahJinPembangun, jumlahJinPengumpul, pasir, batu, air, jinMalas, JinRajin


def TotalJin(array_of_user : list) -> str:
    #Menghitung jumlah jin total

    jumlahJin = 0
    for i in range(Len(array_of_user)): 
        if array_of_user[i][2] == "jin_pembangun" or array_of_user[i][2] == "jin_pengumpul": 
            jumlahJin += 1

    #menghitung jumlah jin pembangun
    jumlahJinPembangun = 0
    for i in range(Len(array_of_user)): 
        if array_of_user[i][2] == "jin_pembangun": 
            jumlahJinPembangun += 1
    
    #menghitung jumlah jin pengumpul 
    jumlahJinPengumpul = 0
    for i in range(Len(array_of_user)): 
        if array_of_user[i][2] == "jin_pengumpul": 
            jumlahJinPengumpul += 1
            
    return jumlahJin, jumlahJinPembangun, jumlahJinPengumpul


def TotalMaterial(array_of_material : list) -> str: 
    pasir = array_of_material[1][2]
    batu = array_of_material[2][2]
    air = array_of_material[3][2]

    return pasir, batu, air

def JinTerajinArray(array_of_user : list, array_of_candi : list) -> list: 
    array_jin_rajin = [None for i in range(Neff)]
    array_jin_rajin[0] = Mark 

    #check dulu di array of user 
    i = 0
    #memasukkan jin pembangun ke dalam array
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == "jin_pembangun":
            tempArr = [array_of_user[i][0], '0', 'jin_pembangun', Mark] 
            Appends(array_jin_rajin, tempArr)
        i += 1

    #memasukkan jin pengumpul ke dalam array
    i = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == "jin_pengumpul":
            tempArr = [array_of_user[i][0], '0', 'jin_pengumpul', Mark] 
            Appends(array_jin_rajin, tempArr)
        i += 1
    jinTermalas = '-'
    jinTerajin = '-'

    if Len(array_jin_rajin) != 0: 
        #menjumlahkan candi yang dibuat jin pembangun ke dalam array 
        for i in range(Len(array_jin_rajin)): 
            for j in range(0, Len(array_of_candi)): 
                if array_jin_rajin[i][0] == array_of_candi[j][1]: 
                    array_jin_rajin[i][1] = str(int(array_jin_rajin[i][1]) + 1)

        #memasukkan jin pembangun yang diubah ke jin pengumpul, tetapi pernah membangun candi
        i = 0
        while array_jin_rajin[i] != Mark : 
            if int(array_jin_rajin[i][1]) == 0 and array_jin_rajin[i][2] == 'jin_pengumpul': 
                array_jin_rajin = Remove(array_jin_rajin, i)
                i = 0
            i += 1
        
        #bublesort untuk mengurutkan array sesuai dengan jumlah candi yang dibuat
        for i in range(Len(array_jin_rajin)): 
            for j in range(Len(array_jin_rajin)- i -1): 
                if int(array_jin_rajin[j+1][1]) > int(array_jin_rajin[j][1]): 
                    array_jin_rajin[j], array_jin_rajin[j+1] = array_jin_rajin[j+1], array_jin_rajin[j]

        #jumlah candi terbanyak dan paling sedikit
        Maks = int(array_jin_rajin[0][1])
        Mins = int(array_jin_rajin[Len(array_jin_rajin)-1][1])
        
        #memasukkan nilai jin yang membangun paling banyak dengan nilai yang sama ke dalam array jin rajin
        jinRajin = [None for i in range(Neff)]
        jinRajin[0] = Mark
        for i in range(Len(array_jin_rajin)): 
            if int(array_jin_rajin[i][1]) == Maks: 
                Appends(jinRajin, array_jin_rajin[i])

        #memasukkan nilai jin yang membangun paling sedikit atau malas dengna nilai yang sama ke dalam array jin malas
        jinMalas = [None for i in range(Neff)]
        jinMalas[0] = Mark
        for i in range(Len(array_jin_rajin)): 
            if int(array_jin_rajin[i][1]) == Mins: 
                Appends(jinMalas, array_jin_rajin[i])

        #sorting leksikografis jinrajin
        for i in range(Len(jinRajin)): 
            for j in range(Len(jinRajin)- i -1): 
                if jinRajin[j][0] > jinRajin[j+1][0]: 
                    jinRajin[j+1], jinRajin[j] = jinRajin[j], jinRajin[j+1]
        
 
        #sorting leksikografis jinmalas
        for i in range(Len(jinMalas)): 
            for j in range(Len(jinMalas)- i -1): 
                if jinMalas[j][0] < jinMalas[j+1][0]: 
                    jinMalas[j+1], jinMalas[j] = jinMalas[j], jinMalas[j+1]
        #memasukkan jin pembangun yang mengubah ke jin pengumpul. Namun, sudan membangun candi
        jinTermalas = jinMalas[0][0]
        jinTerajin = jinRajin[0][0]
    return jinTermalas, jinTerajin

def print_laporan_jin(jumlahJin : str, jumlahJinPembangun : str, jumlahJinPengumpul : str, pasir : str, batu : str, air : str, jinTermalas : str, jinTerajin : str) -> str:      
        print(f"\nJumlah jin: {jumlahJin}")
        print(f"Jumlah jin pengumpul: {jumlahJinPengumpul}")
        print(f"Jumlah jin pembangun: {jumlahJinPembangun}")
        print(f"Jin Terajin: {jinTerajin}")
        print(f"Jin Termalas: {jinTermalas}")
        print(f"Total pasir: {pasir}")
        print(f"Total batu: {batu}")
        print(f"Total air: {air}")
        print("\n")




