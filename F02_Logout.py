from F01_Login import *


def Logout(status_login : bool) -> list: 
    if status_login == True:
        print("\nBerhasil logout dari akun\n")
        return ""
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")