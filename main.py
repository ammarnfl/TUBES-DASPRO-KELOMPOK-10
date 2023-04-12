#Program utama ada disini

#import semua program dari file lain 
import argparse
from os import *
from F01_Login import *
from F02_Logout import *
from F03_SummonJin import *
from F13_Load import *
from Z1_ListFunction import *
from Z2_CSV_Function import *

#inisiasi array sebagai tempat penyimpanan untuk data dari csv
users = [None for i in range(Neff)]
candi = [None for i in range(Neff)]

#argparser untuk mengecek folder ada atau tidak 
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="Usage python3 main.py <nama_folder>")
args = parser.parse_args()

#load : mengambil data dari csv
load(args.nama_folder, 'user.csv', users)


if(os.path.isdir(args.nama_folder) == True): 
    print('Selamat datang di program "Manajerial candi"')
    print("Silahkan masukkan username anda")

    #=============================================================================#
    #============================Program Utama====================================#
    role = ""
    while True: 
        masukkan = input(">>> ")
        if masukkan == "login": 
            if role != "": 
                print(f"Login gagal!\nAnda telah melakukan login dengan username {Username}, silahkan 'logout'")
                print("Sebelum melakukan login kembali")
            while role == "":
                Username = input("username: ")
                Password = input("Password: ")
                role = Login(Username, Password, users)
        elif masukkan == "logout": 
            if role != "":
                role = Logout()
            else: 
                print("Login gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")   
        elif role == "bandung_bondowoso" and masukkan == "summonjin": 
            Summonjin(users)
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
        elif masukkan == "user": 
            print(users)

elif(os.path.isdir(args.nama_folder) == False):
    print(f'Folder "{args.nama_folder}" tidak ditemukan.') 

