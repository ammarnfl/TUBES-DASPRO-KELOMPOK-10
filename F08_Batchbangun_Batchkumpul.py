

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
    total_pasir_needed, total_batu_needed, total_air_needed = 0, 0, 0

    status_pasir = False
    status_batu = False
    status_air = False
    
    #variabel-variabel jin pembangun
    array_of_jin_pembangun = [None for i in range(count+1)]
    array_of_jin_pembangun[0] = Mark
    i = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            array_of_jin_pembangun = Appends(array_of_jin_pembangun, array_of_user[i][0])
        i += 1
    count_jin_pembangun = Len(array_of_jin_pembangun)
    #Generate banyak bahan 
    count_jin = 0
    count_candi = 1
    for j in range(1, Len(array_of_candi)): 
        if Len(array_of_candi[j]) != 1: 
            count_candi += 1 
    for i in range(count): 

        if count_candi <= 100: 
            pasir = randrange(1,5) ; batu = randrange(1,5) ; air = randrange(1,5)
            total_pasir_needed += pasir
            total_batu_needed += batu
            total_air_needed += air 
            count_jin += 1
            count_candi += 1
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
        for i in range(count_jin):
            pasir_needed = array_of_material_needed[i][0]
            batu_needed = array_of_material_needed[i][1]
            air_needed = array_of_material_needed[i][2]

            pasir_have = int(array_of_material[1][2])
            (array_of_material[1][2]) = str(pasir_have - pasir_needed)
            batu_have = int(array_of_material[2][2])
            array_of_material[2][2] = str( batu_have - batu_needed)
            air_have = int(array_of_material[3][2]) 
            array_of_material[3][2] = str( air_have - air_needed)
   
                #membangun candi
            count_candi_append = Len(array_of_candi)
            if count_candi_append == 102: 
                break
            else: 
                z = 0
                status_bangun_kosong = False
                while Marking(array_of_candi[z]) == False: 
                    if Len(array_of_candi[z]) == 1: 
                        array_of_candi[z] = [str(z), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                        status_bangun_kosong = True
                        break
                    z += 1
                if status_bangun_kosong == False: 
                    if Len(array_of_candi) == 1: 
                        candi = [str(count_candi_append), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                    else: 
                        candi = [str(count_candi_append), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                    Appends(array_of_candi, candi)
                    
        #check jumlah candi sebenarnya
        candi_check = 1
        for i in range(1, Len(array_of_candi)): 
            if Len(array_of_candi[i]) != 1: 
                candi_check += 1
        if candi_check == 101: 
            isCandiOver = True
        else: 
            isCandiOver = False
        status_bangun = True
        return array_of_material, array_of_candi, count, count_jin, total_pasir_needed, total_batu_needed, total_air_needed, status_bangun, isCandiOver
    
    #kasus bahan tidak mencukupi
    else:
        candi_check = 1
        for i in range(1, Len(array_of_candi)): 
            if Len(array_of_candi[i]) != 1: 
                candi_check += 1
        if candi_check == 101: 
            isCandiOver = True
        else: 
            isCandiOver = False

        status_bangun = False
        if count == 0: 
            return array_of_material, array_of_candi, count, count_jin, total_air_needed, total_batu_needed, total_air_needed, status_bangun, isCandiOver
        else: 
            pasir_have = int(array_of_material[1][2])
            batu_have = int(array_of_material[2][2])
            air_have = int(array_of_material[3][2]) 
            
            pasir_needed = abs(pasir_have - total_pasir_needed)
            batu_needed = abs(batu_have - total_batu_needed)
            air_needed = abs(air_have - total_air_needed)
            return array_of_material, array_of_candi, count, count_jin, pasir_needed, batu_needed, air_needed, status_bangun, isCandiOver
    