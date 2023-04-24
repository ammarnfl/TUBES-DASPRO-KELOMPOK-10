from Z1_ListFunction import *

def Summonjin(array_of_user : list) -> list: 
    print("\nJenis jin yang dapat dipanggil: ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    while True: 
        jin = (input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        #jin pengumpul
        if jin == "1": 
            role = "jin_pengumpul"            
            print('Memilih jenis jin "Pengumpul"')
            username = input("Masukkan username jin: ")
            while isUsernameExist(username, array_of_user) == True: 
                print(f'Username "{username}"" sudah diambil')
                username = input("Masukkan username jin: ")

            if isUsernameExist(username, array_of_user) == False: 
                while True:
                    password = input("Masukkan password jin: ")
                    if check_password(password) == True: 
                        array_of_user = Appends(array_of_user, [username, password, role, Mark])
                        print("\nHocus Pocus!!!")
                        print("Simsalabim!!!")
                        print("Duarrrr!!!\n")
                        print(f'Jin "{username}" berhasil dipanggil!')
                        break
                    else:
                        print("Password panjangnya harus 5-25 karakter!")
                break 
                   
        #jin pembangun
        elif jin == "2": 
            role = "jin_pembangun"
            print('Memilih jenis jin "Pembangun"')
            username = input("Masukkan username jin: ")
            while isUsernameExist(username, array_of_user) == True: 
                print(f'Username "{username}" sudah diambil')
                username = input("Masukkan username jin: ")

            if isUsernameExist(username, array_of_user) == False: 
                while True:
                    password = input("Masukkan password jin: ")
                    if check_password(password) == True: 
                        array_of_user = Appends(array_of_user, [username, password, role, Mark])
                        print("\nHocus Pocus!!!")
                        print("Simsalabim!!!")
                        print("Duarrrr!!!\n")
                        print(f'Jin "{username}" berhasil dipanggil!')
                        break
                    else:
                        print("Password panjangnya harus 5-25 karakter!")
                break 
       
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
    countjin = 0
    for i in range(Len(arr)): 
        if arr[i][2] == 'jin_pembangun' or arr[i][2] == 'jin_pengumpul': 
            countjin += 1
    return countjin