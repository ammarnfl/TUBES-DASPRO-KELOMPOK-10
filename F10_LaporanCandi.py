from Z1_ListFunction import * 

hargaPasir = 10000
hargaBatu = 15000
hargaAir = 7500

def LaporanCandi(array_of_candi: list) -> str:
    
    Total_candi = 0 
    for i in range(1, Len(array_of_candi)): 
        if Len(array_of_candi[i]) != 1: 
            Total_candi += 1
    
    Total_pasir = 0
    Total_batu = 0
    Total_air = 0
    ID_Candi_termurah = '-'
    ID_Candi_termahal = '-'
    MaksHargaCandi = 0
    MinsHargaCandi = 0

    if Total_candi >= 1: 
        Array_material_candi = [None for i in range(Total_candi + 1)]
        Array_material_candi[0] = Mark
        i = 1
        #mencari total pasir, total batu, total air, assign material ke dalam array 
        while array_of_candi[i] != Mark:
            if Len(array_of_candi[i]) != 1:
                pasir = array_of_candi[i][2]
                batu = array_of_candi[i][3]
                air = array_of_candi[i][4]
                Total_pasir += int(pasir)
                Total_batu += int(batu)
                Total_air += int(air)
                Array_material_candi = Appends(Array_material_candi, [pasir, batu, air, Mark])
            i += 1
        j = 0
        #memasukkan harga masing-masing candi ke dalam sebuah array
        Array_of_hargaCandi = [None for i in range(Total_candi + 1)]
        Array_of_hargaCandi[0] = Mark
        while Array_material_candi[j] != Mark: 
            if Len(array_of_candi[j]) != 1:
                pasirCandi = int(Array_material_candi[j][0])
                batuCandi = int(Array_material_candi[j][1])
                airCandi = int(Array_material_candi[j][2])
                hargaCandi = hargaPasir * pasirCandi + hargaBatu * batuCandi + airCandi *  hargaAir
                Array_of_hargaCandi = Appends(Array_of_hargaCandi, hargaCandi) 
            j += 1
        #mencari nilai maks dan min dari sebuah candi
        MaksHargaCandi = Array_of_hargaCandi[0]
        MinsHargaCandi = Array_of_hargaCandi[0]
        for a in range(Len(Array_of_hargaCandi)): 
            if Array_of_hargaCandi[a] >= MaksHargaCandi: 
                MaksHargaCandi = Array_of_hargaCandi[a]
                ID_Candi_termahal = str(a+1)
            if Array_of_hargaCandi[a] <= MinsHargaCandi: 
                ID_Candi_termurah = str(a+1)
                MinsHargaCandi = Array_of_hargaCandi[a]     
        return Total_candi, Total_pasir, Total_batu, Total_air, ID_Candi_termahal, ID_Candi_termurah, MaksHargaCandi, MinsHargaCandi
    else: 
        Total_candi = 0
        return Total_candi, Total_pasir, Total_batu, Total_air, ID_Candi_termahal, ID_Candi_termurah, MaksHargaCandi, MinsHargaCandi

def print_laporan_candi(totalCandi : str, totalPasir : str, totalBatu : str, totalAir :str, candiTermahal :str,  HargaTermahal : str, candiTermurah : str, HargaTermurah : str) -> str:
    print(f"\n> Total Candi: {totalCandi} ")
    print(f"> Total Pasir yang digunakan: {totalPasir}")
    print(f"> Total Batu yang digunakan: {totalBatu}")
    print(f"> Total Air yang digunakan: {totalAir}")
    print(f"> ID Candi Termahal: {candiTermahal} (Rp{HargaTermahal})")
    print(f"> ID Candi Termurah: {candiTermurah} (Rp{HargaTermurah})\n")