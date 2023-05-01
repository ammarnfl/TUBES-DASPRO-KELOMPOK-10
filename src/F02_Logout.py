from F01_Login import *

#fungsi logout 
def Logout(status_login : bool) -> list: 
    #jika masih login dengan akun lain
    if status_login == True:
        print("Berhasil logout dari akun")
        return ""
    #jika belum login dengan akun manapun
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")