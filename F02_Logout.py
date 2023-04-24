from F01_Login import *


def Logout(status_login : bool) -> list: 
    if Login_status() == True:
        print("\nBerhasil logout dari akun\n")
        return ""