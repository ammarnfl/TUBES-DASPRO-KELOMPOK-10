from F01_Login import *


def Logout(status_login : bool) -> list: 
    if status_login == True:
        print("Berhasil logout dari akun")
        return ""
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")