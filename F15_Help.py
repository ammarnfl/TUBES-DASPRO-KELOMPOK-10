from F01_Login import *

def Help():
    if Login_status() == False:
        print("=========== HELP ===========")
        print("1. login")
        print("untuk masuk menggunakan akun")
        print("2. exit")
        print("untuk keluar dari program dan kembali ke terminal")
    elif Login_status() == False:
        if role == "bandung_bondowoso":
            print("=========== HELP ===========")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin")
            print("untuk memanggil jin dari dunia lain")
            print("3. hapusjin")
            print("untuk mengembalikan jin ke dunia lain")
            print("4. batchkumpul")
            print("mengerahkan seluruh jin untuk mengumpulkan bahan")
            print("5. batchbangun")
            print("mengerahkan seluruh jin untuk membangun candi")
            print("6. laporanjin")
            print("laporan jin untuk mengetahui kinerja jin")
            print("7. laporancandi")
            print("laporan candi untuk mengetahui progress pembangunan candi")
        elif role == "roro_jonggrang":
            print("=========== HELP ===========")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi")
            print("menghancurkan candi yang telah dibangun oleh jin")
            print("3. ayamberkokok")
            print("menyelesaikan permainan")
        elif role == "jin pembangun":
            print("=========== HELP ===========")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. jinpembangun")
            print("membangun candi")
        elif role == "jin pengumpul":
            print("=========== HELP ===========")
            print("1. logout")
            print("untuk keluar dari akun yang digunakan sekarang")
            print("2. jinpengumpul")
            print("mengumpulkan bahan")