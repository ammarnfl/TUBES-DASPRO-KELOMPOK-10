from Z1_ListFunction import *

def Summonjin(array_of_user : list) -> list: 
    print("Jenis jin yang dapat dipanggil: ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    while Len(array_of_user) < 100 + 3: #Syarat jin yang bisa di-summon hanya kurang dari 100 jin
        jin = (input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
        print("")
        #jin pengumpul
        if jin == "1": 
            role = "jin_pengumpul"
            print('Memilih jin jenis "Pengumpul"\n')
            username = input("Masukkan username jin: ")
            while isUsernameExist(username, array_of_user) == True:
                print(f'\nUsername "{username}" sudah diambil!')
                print("Silahkan masukkan username lain!\n")
                username = input("Masukkan username jin: ")    
            while True:
                password = input("Masukkan password jin: ")
                if check_password(password) == True: 
                    array_of_user = Appends(array_of_user, [username, password, role, Mark])
                    break
                else:
                    print("\nPassword panjangnya harus 5-25 karakter!\n") 
            print("\nHocus pocus!!")
            print("Simsalabim!!")
            print("Duarrr!!")
            print(f'\nJin {username} berhasil dipanggil!')
            break
                      
        #jin pembangun
        elif jin == "2": 
            role = "jin_pembangun"
            print('Memilih jin jenis "Pembangun"\n')
            username = input("Masukkan username jin: ")
            while isUsernameExist(username, array_of_user) == True:
                print(f'\nUsername "{username}" sudah diambil!')
                print("Silahkan masukkan username lain!\n")
                username = input("Masukkan username jin: ")    
            while True:
                password = input("Masukkan password jin: ")
                if check_password(password) == True: 
                    array_of_user = Appends(array_of_user, [username, password, role, Mark])
                    break
                else:
                    print("\nPassword panjangnya harus 5-25 karakter!\n")             
            print("\nHocus pocus!!")
            print("Simsalabim!!")
            print("Duarrr!!")
            print(f'\nJin {username} berhasil dipanggil!')
            break
        #     if isUsernameExist(username, array_of_user) == False: 
        #         while True:
        #             password = input("Masukkan password jin: ")
        #             if check_password(password) == True: 
        #                 array_of_user = Appends(array_of_user, [username, password, role, Mark])
        #                 break
        #             else:
        #                 print("Password panjangnya harus 5-25 karakter!")
        #         break 
        #     else: 
        #         print(f"Username {username} sudah diambil")
        #     break
        else: 
            print(f"Tidak ada jenis jin bernomor {jin}!")

        if Len(array_of_user) >= 100 + 3:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung Bondowoso tidak dapat men-summon lebih dari itu")
    return array_of_user
       
def isUsernameExist(username : str, array_of_user : list) -> bool: 
    i = 0
    while array_of_user[i] != Mark: 
        if array_of_user[i][0] == username: 
            return True
        i += 1
    return False

def check_password(password : str) -> bool: 
    if len(password) >= 5 and len(password) <= 25: 
        return True
    return False

def summoned_jin(arr : list) -> int: 
    countjin = Len(arr) - 3
    return countjin