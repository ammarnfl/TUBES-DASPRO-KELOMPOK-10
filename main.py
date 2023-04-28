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
    print("Usage: python main.py <nama_folder>\n")
    exit()
elif(os.path.isdir(args.nama_folder) == True): 
    #load semua file csv ke dalam array 
    load(args.nama_folder, 'user.csv', users)
    load(args.nama_folder, 'candi.csv', candi)
    load(args.nama_folder, 'bahan_bangunan.csv', bahan_bangunan)

 
    print("\nLoading...\n")
    print("\n=========== WELCOME ===========\n\n")
    print('Selamat datang di program "Manajerial candi"')
    print('Masukkan command "help" untuk bantuan sintaks!\n')

    #=============================================================================#
    #============================Program Utama====================================#
    role = ""
    while True: 
        masukkan = input(">>> ")
        #fungsi login 
        if masukkan == "login": 
            if role != "": 
                print(f'\nLogin gagal!\nAnda telah melakukan login dengan username "{Username}", silahkan lakukan "logout" sebelum melakukan login kembali\n')
            while role == "":
                print(" ")
                Username = input("Username: ")
                Password = input("Password: ")
                role = Login(Username, Password, users)

        #fungsi logout
        elif masukkan == "logout": 
            if role != "":
                status_login = Login_status()
                role = Logout(status_login)
            else: 
                print("\nLogout gagal!")
                print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout!!\n") 

        #fungsi summonjin
        elif masukkan == "summonjin": 
            if role == "bandung_bondowoso":
                totalJin = summoned_jin(users)
                print(f'\nJumlah jin saat ini: {totalJin}')
                if totalJin < 100: 
                    print(f"Tersisa {100-totalJin} jin yang bisa dipanggil")
                    Summonjin(users)
                else: 
                    print("\nJumlah Jin telah maksimal! (100 jin)\nBandung tidak dapat men-summon lebih dari itu\n")
            else:
                print('\nMaaf, perintah "summonjin" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')

        #fungsi hapus jin
        elif masukkan == "hapusjin":
            if role == "bandung_bondowoso":
                username_jin = input("\nMasukkan username jin: ")
                users = HapusJin(users, username_jin)
                candi = HapusJinCandi(candi, username_jin)
            else: 
                print('\nMaaf, perintah "hapusjin" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')

        elif masukkan == "ubahjin":
            if role == "bandung_bondowoso":
                ubah_jin(users)
            else: 
                print('\nMaaf, perintah "ubahjin" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')

        #fungsi bangun
        elif  masukkan == "bangun": 
            if role == "jin_pembangun": 
                (candi, bahan_bangunan) = Jin_Pembangun(candi, bahan_bangunan, Username)
            else: 
                print('\nMaaf, perintah "bangun" hanya bisa dilakukan apabila telah login menggunakan akun "Jin Pembangun"\n')

        #fungsi kumpul
        elif masukkan == "kumpul": 
            if role == "jin_pengumpul":
                (bahan_bangunan, pasir, batu, air) = CollectMaterial(bahan_bangunan)
                print(f"\nJin menemukan {pasir} pasir, {batu} batu, dan {air} air\n")
            else: 
                print('\nMaaf, perintah "kumpul" hanya bisa dilakukan apabila telah login menggunakan akun "Jin Pengumpul"\n')
        #fungsi batchkumpul

        elif masukkan == "batchkumpul":  
            if role == "bandung_bondowoso": 
                (bahan_bangunan, jumlah_jin_pengumpul, pasir, batu, air) = Batch_kumpul(users, bahan_bangunan)
                if jumlah_jin_pengumpul == 0: 
                    print('\nGagal mengumpulkan bahan. Anda tidak memiliki jin pengumpul.\nSilahkan masukkan perintah "summonjin" terlebih dahulu untuk memanggil jin "Pengumpul"\n')
                else: 
                    print(f"\nMengerahkan {jumlah_jin_pengumpul} jin pengumpul untuk mengumpulkan bahan")
                    print(f"\nJin menemukan {pasir} pasir, {batu} batu, dan {air} air\n")
            else: 
                print('\nMaaf, perintah "batchkumpul" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')
        #fungsi batchbangun
        elif masukkan == "batchbangun": 
            if role == "bandung_bondowoso": 
                (bahan_bangunan, candi, jumlah_jin, pasir, batu, air, status_bangun, isCandiOver) = Batch_bangun(users, candi, bahan_bangunan)
                if jumlah_jin == 0: 
                    print("\nBangun gagal. Anda tidak punya jin pembangun. Silahkan summon jin terlebih dahulu!\n")
                else: 
                    if status_bangun == True: 
                        if isCandiOver == True: 
                            print("\nMisi berhasil!! 100 candi berhasil dibangun!!\n")
                        else: 
                            print(f"\nMengerahkan {jumlah_jin} jin pembangun untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, dan {air} air")
                            print(f'\n{jumlah_jin} candi berhasil dibangun!\n')
                    else:
                        if isCandiOver == True: 
                            print("\nBangun gagal\n")
                        else:
                            print(f"\nBangun gagal! Kurang {pasir} pasir, {batu} batu, dan {air} air ")
                            print('\nSilahkan masukkan perintah "batchkumpul" untuk mengumpulkan bahan\n')
            else: 
                print('\nMaaf, perintah "batchbangun" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')
              
        #fungsi laporan jin 
        elif masukkan == "laporanjin": 
            if role == "bandung_bondowoso":
                jumlahJin, jumlahJinPembangun, jumlahJinPengumpul, pasir, batu, air, jinMalas, jinRajin = LaporanJin(users, bahan_bangunan, candi)
                print_laporan_jin(jumlahJin, jumlahJinPembangun, jumlahJinPengumpul, pasir, batu, air, jinMalas, jinRajin)
            else: 
                print('\nMaaf, perintah "laporanjin" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')

        #fungsi laporan candi
        elif masukkan == "laporancandi": 
            if role == "bandung_bondowoso":
                totalCandi, totalPasir, totalBatu, totalAir, candiTermahal, candiTermurah, HargaTermahal, HargaTermurah  = LaporanCandi(candi)
                print_laporan_candi(totalCandi, totalPasir, totalBatu, totalAir, candiTermahal, HargaTermahal, candiTermurah, HargaTermurah )
            else: 
                print('\nMaaf, perintah "laporancandi" hanya bisa dilakukan apabila telah login menggunakan akun "Bandung Bondowoso"\n')   
        #fungsi Roro Jonggrang
        #fungsi hancurkancandi
        elif masukkan == "hancurkancandi":
            if role == "roro_jonggrang":
                id_candi = input("\nMasukkan ID candi: ")
                candi = HancurkanCandi(candi, id_candi)
            else:
                print('\nMaaf, perintah "hancurkancandi" hanya bisa dilakukan apabila telah login menggunakan akun "Roro Jonggrang"\n')
        
        #fungsi ayamberkokok
        elif masukkan == "ayamberkokok": 
            if role == "roro_jonggrang":
                AyamBerkokok(candi)
            else: 
              print('\nMaaf, perintah "ayamberkokok" hanya bisa dilakukan apabila telah login menggunakan akun "Roro Jonggrang"\n')  
    
        elif masukkan == "help": 
            Help(role)
            
        #fungsi Save
        elif masukkan == "save": 
            parent = "data"
            folderpath = input("\nMasukkan nama folder: ")
            print("\nSaving...\n")
            folder = parent + "/" + folderpath
            save(folder, users, 'user.csv')
            save(folder, candi, 'candi.csv')
            save(folder, bahan_bangunan, 'bahan_bangunan.csv')
            print(f"Menyimpan folder di {folder}...\n")
        #fungsi exit

        else: 
            print('\nInput tidak sesuai\nKetik "help" untuk tahu command yang bisa digunakan\n')

elif(os.path.isdir(args.nama_folder) == False):
    print(f'\nFolder "{args.nama_folder}" tidak ditemukan.') 

