

from random import * 
from Z1_ListFunction import *

def Batch_kumpul(array_of_user : list, array_of_material : list) -> list:
    role = "jin_pengumpul"
    i = 0
    count = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            count += 1
        i += 1
    pasir, batu, air = 0, 0, 0
    for i in range(count):  
        pasir += randrange(0,5)
        batu += randrange(0,5)
        air += randrange(0,5)

    array_pasir = ['pasir', 'PerluNih!', str(pasir), Mark]
    array_batu = ['batu', 'KerasCuy', str(batu), Mark]
    array_air = ['air', 'Enak nih diminum', str(air), Mark]
    if Len(array_of_material) == 1: 
        array_of_material = Appends(array_of_material, array_pasir)
        array_of_material = Appends(array_of_material, array_batu)
        array_of_material = Appends(array_of_material, array_air)
    else: 
        i = 0
        while Marking(array_of_material[i]) != True: 
            j = 0
            if array_of_material[i][j] == 'pasir': 
                array_of_material[i][2] = str(int(array_of_material[i][2]) + pasir)
            elif array_of_material[i][j] == 'batu':
                array_of_material[i][2] = str(int(array_of_material[i][2]) + batu)
            elif array_of_material[i][j] == 'air': 
                array_of_material[i][2] = str(int(array_of_material[i][2]) + air)
            i += 1
    return array_of_material, count, pasir, batu, air


#array_of_material, array_of_candi, count, count_jin, total_pasir_needed, total_batu_needed, total_air_needed, status_bangun
def Batch_bangun(array_of_user : list, array_of_candi : list, array_of_material : list) -> list: 
    role = "jin_pembangun"
    i = 0
    count = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            count += 1
        i += 1
    #variabel-variabel material
    array_of_material_needed = [None for i in range(count + 1)]
    array_of_material_needed[0] = Mark
    total_pasir_needed, total_batu_needed, total_air_needed, total_bahan = 0, 0, 0, 0

    status_pasir = False
    status_batu = False
    status_air = False
    
    #variabel-variabel jin pembangun
    array_of_jin_pembangun = [None for i in range(count+1)]
    array_of_jin_pembangun[0] = Mark
    i = 0
    #memasukkan jin_pembangun ke dalam array_of_jin_pembangun
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            array_of_jin_pembangun = Appends(array_of_jin_pembangun, array_of_user[i][0])
        i += 1
    
    #menghitung berapa banyak candi yang perlu dibuat
    for i in range(count): 
            pasir = randrange(1,5) ; batu = randrange(1,5) ; air = randrange(1,5)
            total_pasir_needed += pasir
            total_batu_needed += batu
            total_air_needed += air 
            material_needed = [pasir, batu, air, Mark]
            array_of_material_needed = Appends(array_of_material_needed, material_needed)
    #membandingkan nilai total bahan dibutuhkan dengan total bahan dipunya

    if Len(array_of_material) != 1: 
        if int(array_of_material[1][2]) >= total_pasir_needed:
            status_pasir = True
        if int(array_of_material[2][2]) >= total_batu_needed:  
            status_batu = True
        if int(array_of_material[3][2]) >= total_air_needed:
            status_air = True

    #jika kasus semua bahan cukup
    if status_air == True and status_batu == True and status_pasir == True: 
        #mengurangi bahan
        jumlahJinDipakai = 0
        for i in range(count):
            pasir_needed = int(array_of_material_needed[i][0])
            batu_needed = int(array_of_material_needed[i][1])
            air_needed = int(array_of_material_needed[i][2])

            pasir_have = int(array_of_material[1][2])
            (array_of_material[1][2]) = str(pasir_have - pasir_needed)
            batu_have = int(array_of_material[2][2])
            array_of_material[2][2] = str( batu_have - batu_needed)
            air_have = int(array_of_material[3][2]) 
            array_of_material[3][2] = str(air_have - air_needed)

        
        #membangun candi
        for i in range(count):
            pasir_needed = array_of_material_needed[i][0]
            batu_needed = array_of_material_needed[i][1]
            air_needed = array_of_material_needed[i][2]

            count_candi_append = Len(array_of_candi)
            if count_candi_append == 101: 
                id_check = 0
                while Marking(array_of_candi[id_check]) == False: 
                    if Len(array_of_candi[id_check]) == 1: 
                        array_of_candi[id_check] = [str(id_check), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                        jumlahJinDipakai += 1
                    id_check += 1
                break
            else: 
                jumlahJinDipakai += 1
                z = 0
                status_bangun_kosong = False
                #algoritma yang mengisi array candi bagian kosong terlebih dahulu
                while Marking(array_of_candi[z]) == False: 
                    if Len(array_of_candi[z]) == 1: 
                        array_of_candi[z] = [str(z), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                        status_bangun_kosong = True
                        break
                    z += 1
                #algoritma yang menambah baris pada csv atau array
                if status_bangun_kosong == False: 
                    if Len(array_of_candi) == 1: 
                        candi = [str(count_candi_append), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                    else: 
                        candi = [str(count_candi_append), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                    Appends(array_of_candi, candi)

        #check jumlah candi sebenarnya
        candi_check = 0
        for i in range(Len(array_of_candi)): 
            if Len(array_of_candi[i]) != 1: 
                candi_check += 1
        candi_check -= 1

        #apakah candi sudah berjumlah 100? 
        if candi_check == 100 and jumlahJinDipakai == 0: 
            isCandiOver = True
        else: 
            isCandiOver = False
        
        status_bangun = True
        return array_of_material, array_of_candi, count, total_pasir_needed, total_batu_needed, total_air_needed, status_bangun, isCandiOver
    
    #kasus bahan tidak mencukupi
    else:
        candi_check = 0
        for i in range(Len(array_of_candi)): 
            if Len(array_of_candi[i]) != 1: 
                candi_check += 1
        candi_check -= 1

        if candi_check == 100: 
            isCandiOver = True
        else: 
            isCandiOver = False

        status_bangun = False
        if count == 0: 
            return array_of_material, array_of_candi, count, total_air_needed, total_batu_needed, total_air_needed, status_bangun, isCandiOver
        
        else: 
            pasir_needed, batu_needed, air_needed = 0, 0, 0
            pasir_have = int(array_of_material[1][2])
            batu_have = int(array_of_material[2][2])
            air_have = int(array_of_material[3][2]) 

            if status_pasir == False:
                pasir_needed = Absolute(pasir_have - total_pasir_needed)
            if status_batu == False: 
                batu_needed = Absolute(batu_have - total_batu_needed)
            if status_air == False:
                air_needed = Absolute(air_have - total_air_needed)
            return array_of_material, array_of_candi, count, pasir_needed, batu_needed, air_needed, status_bangun, isCandiOver
    
