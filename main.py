#Program utama ada disini

#import semua program dari file lain 
import argparse
from os import *
from F01_Login import *
from F02_Logout import *
from F03_SummonJin import *
from F04_HapusJin import *
from F05_UbahJin import *
from F06_JinPembangun import *
from F07_JinPengumpul import *
from F13_Load import *
from F14_Save import *
from Z1_ListFunction import *
from Z2_CSV_Function import *


#inisiasi array sebagai tempat penyimpanan untuk data dari csv
users = [None for i in range(Neff)]
candi = [None for i in range(Neff)]
bahan_bangunan = [None for i in range(Neff)]


#argparser untuk mengecek folder ada atau tidak 
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="Usage python3 main.py <nama_folder>")
args = parser.parse_args()

#load : mengambil data dari csv
load(args.nama_folder, 'user.csv', users)
load(args.nama_folder, 'candi.csv', candi)
load(args.nama_folder, 'bahan_bangunan.csv', bahan_bangunan)

if(os.path.isdir(args.nama_folder) == True): 
    print(array_eff_None(users))
    print('Selamat datang di program "Manajerial candi"')
    print("Silahkan masukkan username anda")

    #=============================================================================#
    #============================Program Utama====================================#
    role = ""
    while True: 
        masukkan = input(">>> ")
        #fungsi login 
        if masukkan == "login": 
            if role != "": 
                print(f"Login gagal!\nAnda telah melakukan login dengan username {Username}, silahkan 'logout'")
                print("Sebelum melakukan login kembali")
            while role == "":
                Username = input("username: ")
                Password = input("Password: ")
                role = Login(Username, Password, users)
        #fungsi logout
        elif masukkan == "logout": 
            if role != "":
                role = Logout()
            else: 
                print("Login gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")   
        #fungsi summonjin
        elif role == "bandung_bondowoso" and masukkan == "summonjin": 
            Summonjin(users)
        #fungsi hapus jin
        elif role == "bandung_bondowoso" and masukkan == "hapusjin": 
            username_jin = input("Masukkan username jin: ")
            users = HapusJin(users, username_jin)
            candi = HapusJinCandi(candi, username_jin)
        #fungsi ubah tipe jin
        elif role == "bandung_bondowoso" and masukkan == "ubahjin": 
            ubah_jin(users)
        
        elif role == "jin_pembangun" and masukkan == "bangun": 
            (candi, bahan_bangunan) = Jin_Pembangun(candi, bahan_bangunan, Username)
        elif role == "jin_pengumpul" and masukkan == "kumpul":
            (bahan_bangunan, pasir, batu, air) = CollectMaterial(bahan_bangunan)
            print(f"Jin menemukan {pasir} pasir {batu} batu {air} air")
        elif role == "roro_jonggrang":
            print()
        elif masukkan == "help": 
            print()
        elif masukkan == "save" and role != "": 
            folder = input("Masukkan nama folder: ")
            save(folder, users, 'user.csv')
            save(folder, candi, 'candi.csv')
            save(folder, bahan_bangunan, 'bahan_bangunan.csv')
        elif masukkan == "exit": 
            exit()
        elif masukkan == "user": 
            print(array_eff_None(users))
        elif masukkan == "bahan": 
            print(array_eff_None(bahan_bangunan))
        elif masukkan == "candi":
            print(array_eff_None(candi))

elif(os.path.isdir(args.nama_folder) == False):
    print(f'Folder "{args.nama_folder}" tidak ditemukan.') 

