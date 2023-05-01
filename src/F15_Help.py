from F01_Login import *
def Help(role : str) -> str:
    #akun belum login sama sekali
    if role == "":
        print("\n=========== HELP ===========\n")
        print("1. login")
        print("untuk masuk menggunakan akun")
        print("2. exit")
        print("untuk keluar dari program dan kembali ke terminal")
        print(" ")
    #akun yang sudah login
    elif Login_status() == True:
        #akun bandung bondowoso
        if role == "bandung_bondowoso":
            print("\n=========== HELP ===========\n")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin")
            print("untuk memanggil jin dari dunia lain")
            print("3. hapusjin")
            print("untuk mengembalikan jin ke dunia lain")
            print("4. ubahjin")
            print("untuk mengubah tipe jin")
            print("5. batchkumpul")
            print("untuk mengerahkan seluruh jin untuk mengumpulkan bahan")
            print("6. batchbangun")
            print("untuk mengerahkan seluruh jin untuk membangun candi")
            print("7. laporanjin")
            print("untuk mengetahui kinerja jin")
            print("8. laporancandi")
            print("untuk mengetahui progress pembangunan candi")
            print("9. save")
            print("untuk melakukan penyimpanan")
            print("10. exit")
            print("untuk keluar dari program")
            print(" ")
        #akun Roro Jonggrang
        elif role == "roro_jonggrang":
            print("\n=========== HELP ===========\n")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi")
            print("untuk menghancurkan candi yang telah dibangun oleh jin")
            print("3. ayamberkokok")
            print("untuk menyelesaikan permainan")
            print("4. save")
            print("untuk melakukan penyimpanan")
            print("5. exit")
            print("untuk keluar dari program")
            print(" ")
        #akun jin pembangun
        elif role == "jin_pembangun":
            print("\n=========== HELP ===========\n")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("untuk membangun candi")
            print("3. save")
            print("untuk melakukan penyimpanan")
            print("4. exit")
            print("untuk keluar dari program")
            print(" ")
        #akun jin pengumpul
        elif role == "jin_pengumpul":
            print("\n=========== HELP ===========\n")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print("untuk mengumpulkan bahan")
            print("3. save")
            print("untuk melakukan penyimpanan")
            print("4. exit")
            print("untuk keluar dari program")
            print(" ")