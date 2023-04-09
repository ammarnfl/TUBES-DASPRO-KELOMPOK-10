import csv

def Summonjin(): 
    user_jin = ["", "", ""]
    f = open('user.csv', 'r+', newline='')
    reader = csv.reader(f)
    writer = csv.writer(f, delimiter=';')
    print("Jenis jin yang dapat dipanggil: ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    while True: 
        role = "jin_pengumpul"
        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        #jin pengumpul
        if jin == 1: 
            print("memilih jin pengumpul.")
            username = input("Masukkan username jin: ")

            if check_username(username) == False: 
                user_jin[0] = username
                while True:
                    password = input("Masukkan password jin: ")
                    if check_password(password) == True: 
                        user_jin[1] = password
                        user_jin[2] = role
                        for row in reader:
                            if row: 
                                writer.writerow(user_jin)
                                break
                        break
                    else:
                        print("Password panjangnya harus 5-25 karakter!")
                break 
            else: 
                print(f"username {username} sudah diambil")
            
        #jin pembangun
        elif jin == 2: 
            role = "jin_pembangun"
            print("memilih jin pembangun.")
            username = input("Masukkan username jin: ")
            if check_username(username) == False: 
                user_jin[0] = username
                while True:
                    password = input("Masukkan password jin: ")
                    if check_password(password) == True: 
                        user_jin[1] = password
                        user_jin[2] = role
                        for row in reader:
                            if row: 
                                writer.writerow(user_jin)
                                break
                        break
                    else:
                        print("Password panjangnya harus 5-25 karakter!")
                break 
            else: 
                print(f"username {username} sudah diambil")

            break
        else: 
            print(f"tidak ada jenis jin bernomor {jin}!")
        
def check_username(username): 
    f = open('user.csv', 'r+')
    reader = csv.reader(f, delimiter =';')

    for row in reader: 
        if row[0] == username: 
            f.close()
            return True
    f.close()
    return False


def check_password(password): 
    if len(password) >= 5 and len(password) <= 25: 
        return True
    return False