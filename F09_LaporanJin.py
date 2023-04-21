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
    array_jin_rajin = [None for i in range(50)]
    array_jin_rajin[0] = Mark 

    #check dulu di array of user 
    i = 0
    #memasukkan jin pembangun ke dalam array
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == "jin_pembangun":
            tempArr = [array_of_user[i][0], '0', 'jin_pembangun', Mark] 
            Appends(array_jin_rajin, tempArr)
        i += 1
    
    i = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == "jin_pengumpul":
            tempArr = [array_of_user[i][0], '0', 'jin_pengumpul', Mark] 
            Appends(array_jin_rajin, tempArr)
        i += 1

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
    jinRajin = [None for i in range(101)]
    jinRajin[0] = Mark
    for i in range(Len(array_jin_rajin)): 
        if int(array_jin_rajin[i][1]) == Maks: 
            Appends(jinRajin, array_jin_rajin[i])

    #memasukkan nilai jin yang membangun paling sedikit atau malas dengna nilai yang sama ke dalam array jin malas
    jinMalas = [None for i in range(101)]
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


bruh = [['username', 'password', 'role', -9999], ['Bondowoso', 'cintaroro', 'bandung_bondowoso', -9999], ['Roro', 'gasukabondo', 'roro_jonggrang', -9999], ['waduh', '12345', 'jin_pengumpul', -9999], ['waduh4', '12345', 'jin_pengumpul', -9999], ['waduhhabis', '12345', 'jin_pengumpul', -9999], ['waduh1', 'saves', 'jin_pengumpul', -9999], ['waduh2', 'saves', 'jin_pembangun', -9999], ['waduh3', 'saves', 'jin_pembangun', -9999], ['waduh4', 'saves', 'jin_pembangun', -9999], ['waduh5', 'saves', 'jin_pembangun', -9999], ['waduh6', 'saves', 'jin_pembangun', -9999], -9999]
candi = [['id', 'pembuat', 'pasir', 'batu', 'air', -9999], ['1', 'waduh1', '2', '4', '1', -9999], ['2', 'waduh2', '3', '3', '2', -9999], ['3', 'waduh3', '3', '1', '3', -9999], ['4', 'waduh4', '1', '3', '4', -9999], ['5', 'waduh5', '3', '3', '1', -9999], ['6', 'waduh6', '4', '3', '4', -9999], ['7', 'waduh1', '1', '1', '2', -9999], ['8', 'waduh2', '1', '2', '4', -9999], ['9', 'waduh3', '3', '2', '3', -9999], ['10', 'waduh4', '3', '4', '3', -9999], ['11', 'waduh5', '1', '3', '3', -9999], ['12', 'waduh6', '4', '3', '3', -9999], ['13', 'waduh1', '2', '4', '2', -9999], ['14', 'waduh2', '3', '1', '4', -9999], ['15', 'waduh3', '3', 
'4', '2', -9999], ['16', 'waduh4', '2', '4', '4', -9999], ['17', 'waduh5', '1', '3', '3', -9999], ['18', 'waduh6', '3', '2', '2', -9999], ['19', 'waduh1', '2', '4', '4', -9999], ['20', 'waduh2', '3', '1', '1', -9999], ['21', 'waduh3', '2', '4', '4', -9999], ['22', 'waduh4', '2', '1', '4', -9999], ['23', 'waduh5', '3', '4', '1', -9999], ['24', 'waduh6', '1', '3', '2', -9999], ['25', 'waduh1', '1', '3', '1', -9999], ['26', 'waduh2', '1', '2', '2', -9999], ['27', 'waduh3', '2', '2', '3', -9999], ['28', 'waduh4', '3', '4', '1', -9999], ['29', 'waduh5', '2', '2', '3', -9999], ['30', 'waduh6', '2', '3', '4', -9999], ['31', 'waduh1', '1', '1', '1', -9999], ['32', 'waduh2', '1', '3', '3', -9999], ['33', 'waduh3', '1', '2', '4', -9999], ['34', 'waduh4', '2', '2', '2', -9999], ['35', 'waduh5', '4', '3', '3', -9999], ['36', 'waduh6', '1', '2', '3', -9999], ['37', 'waduh1', '3', '3', '4', -9999], ['38', 'waduh2', '2', '3', '3', -9999], ['39', 'waduh3', '1', '3', '4', -9999], ['40', 'waduh4', '2', '2', '4', -9999], ['41', 'waduh5', '4', '4', '3', -9999], ['42', 'waduh6', '2', '3', '2', -9999], ['43', 'waduh1', '4', '3', '1', -9999], ['44', 'waduh2', '4', '2', '1', -9999], ['45', 'waduh3', '3', '4', '2', -9999], ['46', 'waduh4', '2', '1', '3', -9999], ['47', 'waduh5', '1', '3', '3', -9999], ['48', 'waduh6', '2', '1', '1', -9999], ['49', 'waduh1', '4', '2', '4', -9999], ['50', 'waduh2', '4', '3', '1', -9999], ['51', 'waduh3', '4', '1', '4', -9999], ['52', 'waduh4', '4', '3', '4', -9999], ['53', 'waduh5', '1', '3', '1', -9999], ['54', 'waduh6', '2', 
'4', '1', -9999], ['55', 'waduh1', '1', '2', '3', -9999], ['56', 'waduh2', '4', '1', '1', -9999], ['57', 'waduh3', '3', '3', '2', -9999], ['58', 'waduh4', '4', '1', '3', -9999], ['59', 'waduh5', '2', '1', '4', -9999], ['60', 'waduh6', '2', '2', '2', -9999], ['61', 'waduh1', '4', '2', '1', -9999], ['62', 'waduh2', '4', '4', '1', -9999], ['63', 'waduh3', '4', '1', '4', -9999], ['64', 'waduh4', '4', '2', '2', -9999], ['65', 'waduh5', '2', '1', '3', -9999], ['66', 'waduh6', '4', '3', '4', -9999], ['67', 'waduh1', '4', '4', '2', -9999], ['68', 'waduh2', '3', '2', '2', -9999], ['69', 'waduh3', '2', '1', '1', -9999], ['70', 'waduh4', '3', '3', '2', -9999], ['71', 'waduh5', '1', '3', '1', -9999], ['72', 'waduh6', '3', '1', '4', -9999], ['73', 'waduh1', '2', '2', '1', -9999], ['74', 'waduh2', '2', '2', '4', -9999], ['75', 'waduh3', '3', '3', '2', -9999], ['76', 'waduh4', '3', '4', '2', -9999], ['77', 'waduh5', '4', '3', '3', -9999], ['78', 'waduh6', '1', '2', '4', -9999], ['79', 'waduh1', '3', '4', '2', -9999], ['80', 'waduh2', '3', '2', '4', -9999], ['81', 'waduh3', '2', '3', '1', -9999], ['82', 'waduh4', '4', '4', '2', -9999], ['83', 'waduh5', '4', '4', '1', -9999], ['84', 'waduh6', '3', '1', '3', -9999], ['85', 'waduh1', '1', '3', '2', -9999], ['86', 'waduh2', '4', '1', '2', -9999], ['87', 'waduh3', '2', '4', '4', -9999], ['88', 'waduh4', '4', '2', '4', -9999], ['89', 'waduh5', '1', '1', '4', -9999], ['90', 'waduh6', '3', '4', '3', -9999], ['91', 'waduh1', '4', '4', '1', -9999], ['92', 'waduh2', '1', '1', '1', -9999], ['93', 'waduh3', '2', 
'2', '4', -9999], ['94', 'waduh4', '3', '1', '3', -9999], ['95', 'waduh5', '3', '3', '1', -9999], ['96', 'waduh6', '1', '3', '4', -9999], ['97', 'waduh1', '4', '4', '1', -9999], ['98', 'waduh1', '4', '4', '1', -9999], ['99', 'waduh1', '2', '2', '2', -9999], ['100', 'waduh4', '3', '1', '1', -9999], -9999] 
a = [None for i in range(Neff)]
a = JinTerajinArray(bruh, candi)

