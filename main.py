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
from F08_Batchbangun_Batchkumpul import *
from F09_LaporanJin import *
from F10_LaporanCandi import *
from F11_HancurkanCandi import *
from F12_AyamBerkokok import *
from F13_Load import *
from F14_Save import *
from F15_Help import *
from F16_Exit import *
from Z1_ListFunction import *
from Z2_CSV_Function import *


#inisiasi array sebagai tempat penyimpanan untuk data dari csv
users = [None for i in range(Neff)]
candi = [None for i in range(Neff)]
bahan_bangunan = [None for i in range(Neff)]


#argparser untuk mengecek folder ada atau tidak 
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", nargs ='?', help="Usage python3 main.py <nama_folder>")
args = parser.parse_args()
#load : mengambil data dari csv

if args.nama_folder == None: 
    print("\nTidak ada nama folder yang diberikan!\n")
    print("Usage: python main.py <nama_folder>")
    exit()
elif(os.path.isdir(args.nama_folder) == True): 
    load(args.nama_folder, 'user.csv', users)
    load(args.nama_folder, 'candi.csv', candi)
    load(args.nama_folder, 'bahan_bangunan.csv', bahan_bangunan)

    #print(array_eff_None(users))
    print('Selamat datang di program "Manajerial candi"')
    print("Help untuk bantuan sintaks")

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
                status_login = Login_status()
                role = Logout(status_login)
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

        #fungsi bangun
        elif role == "jin_pembangun" and masukkan == "bangun": 
            (candi, bahan_bangunan) = Jin_Pembangun(candi, bahan_bangunan, Username)

        #fungsi kumpul
        elif role == "jin_pengumpul" and masukkan == "kumpul":
            (bahan_bangunan, pasir, batu, air) = CollectMaterial(bahan_bangunan)
            print(f"Jin menemukan {pasir} pasir {batu} batu {air} air")

        #fungsi batchkumpul
        elif role == "bandung_bondowoso" and masukkan == "batchkumpul":  
            (bahan_bangunan, jumlah_jin_pengumpul, pasir, batu, air) = Batch_kumpul(users, bahan_bangunan)
            if jumlah_jin_pengumpul == 0: 
                print("Kumpul gagal. Anda tidak memiliki jin pengumpul, summonjin pengumpul terlebih dahulu")
            else: 
                print(f"Mengerahkan {jumlah_jin_pengumpul} untuk mengumpulkan bahan ")
                print(f"Jin menemukan {pasir} pasir {batu} batu {air} air")

        #fungsi batchbangun
        elif role == "bandung_bondowoso" and masukkan == "batchbangun": 
            (bahan_bangunan, candi, jumlah_jin, pasir, batu, air, status_bangun, isCandiOver) = Batch_bangun(users, candi, bahan_bangunan)
            if jumlah_jin == 0: 
                print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
            else: 
                if status_bangun == True: 
                    if isCandiOver == True: 
                        print("Bangun berhasil")
                    else: 
                        print(f"Mengerahkan {jumlah_jin} jin untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, {air} air")
                else:
                    if isCandiOver == True: 
                        print("Bangun gagal")
                    else:
                        print(f"Bangun gagal. Kurang {pasir} pasir, {batu} batu, {air} air ") 
              
        #fungsi laporan jin 
        elif role == "bandung_bondowoso" and masukkan == "laporanjin": 
            jumlahJin, jumlahJinPembangun, jumlahJinPengumpul, pasir, batu, air, jinMalas, jinRajin = LaporanJin(users, bahan_bangunan, candi)
            print_laporan_jin(jumlahJin, jumlahJinPembangun, jumlahJinPengumpul, pasir, batu, air, jinMalas, jinRajin)


        #fungsi laporan candi
        elif role == "bandung_bondowoso" and masukkan == "laporancandi": 
            totalCandi, totalPasir, totalBatu, totalAir, candiTermahal, candiTermurah, HargaTermahal, HargaTermurah  = LaporanCandi(candi)
            print_laporan_candi(totalCandi, totalPasir, totalBatu, totalAir, candiTermahal, HargaTermahal, candiTermurah, HargaTermurah )
                
        #fungsi Roro Jonggrang
        #fungsi hancurkancandi
        elif role == "roro_jonggrang" and masukkan == "hancurkancandi":
            id_candi = input("Masukkan ID candi: ")
            candi = HancurkanCandi(candi, id_candi)
        
        #fungsi ayamberkokok
        elif role == "roro_jonggrang" and masukkan == "ayamberkokok": 
            AyamBerkokok(candi)
    
        elif masukkan == "help": 
            Help(role)
            
        #fungsi Save
        elif masukkan == "save": 
            parent = "data"
            folderpath = input("Masukkan nama folder: ")
            folder = parent + "/" + folderpath
            save(folder, users, 'user.csv')
            save(folder, candi, 'candi.csv')
            save(folder, bahan_bangunan, 'bahan_bangunan.csv')
            print(f"Menyimpan folder di {folder}...")
        #fungsi exit
        elif masukkan == "exit": 
            Exit(users, candi, bahan_bangunan)
            print(f"Menyimpan folder di {path}...")
        #buat debugging
        elif masukkan == "user": 
            print(array_eff_None(users))
        elif masukkan == "bahan": 
            print(array_eff_None(bahan_bangunan))
        elif masukkan == "candi":
            print(array_eff_None(candi))
        elif masukkan == "jumlahcandi": 
            count_candi = 0
            for i in range(1, Len(candi)): 
                if Len(candi[i]) != 1: 
                    count_candi += 1
            print(count_candi)

elif(os.path.isdir(args.nama_folder) == False):
    print(f'Folder "{args.nama_folder}" tidak ditemukan.') 

