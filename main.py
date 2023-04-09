#Program utama ada disini
from F01_Login import Login
from F02_Logout import Logout

from helps import *

def main():
    role = ""
    while True: 
        masukkan = input(">>> ")
        if masukkan == "login": 
            print(role)
            if role != "": 
                print(f"Login gagal!\nAnda telah melakukan login dengan username {Username}, silahkan 'logout'")
                print("Sebelum melakukan login kembali")
            while role =="":
                Username = input("username: ")
                Password = input("Password: ")
                role = Login(Username, Password)
        elif masukkan == "logout": 
            if role != "":
                role = Logout()
            else: 
                print("Login gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")        
        elif role == "jin_pembangun" and masukkan == "bangun": 
            print()
        elif role == "jin_pengumpul" and masukkan == "kumpul":
            print()
        elif role == "roro_jonggrang":
            print()
        elif masukkan == "help": 
            print()
        elif masukkan == "exit": 
            exit()

    
main()

