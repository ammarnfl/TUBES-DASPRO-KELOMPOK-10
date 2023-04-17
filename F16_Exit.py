from F01_Login import *
from F14_Save import *
from Z1_ListFunction import *

def exit( ):
    while login_status == True:
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

        if simpan == 'n' or simpan == 'N':
            exit
        elif simpan == 'y' or simpan == 'Y':
            save()
        else:
            simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    return exit        

