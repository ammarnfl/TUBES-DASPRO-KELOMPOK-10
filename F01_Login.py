import csv 
from OurFunction import *
from Z1_ListFunction import *


def Login(username : str, password : str, array_of_user : list) -> str:
    global login_status
    login_status = False
    #check username 
    i = 0 
    while array_of_user[i] != Mark: 
        if array_of_user[i][0] == username: 
            if array_of_user [i][1] == password: 
                login_status = True 
                role = array_of_user[i][2]
                break
            else: 
                login_status = False
                break
        i += 1
    if array_of_user[i] == Mark: 
        print("Username tidak terdaftar!")
        role = ""
        return role
    else:
        if login_status == False: 
            print("Password salah!")
            role = ""
            return role
        else: 
            print(f"Selamat datang, {username}")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil')
            return role

    """#check username dan password ada atau tidak
    for row in reader: 
        if row[0] == username: 
            if row[1] == password: 
                login_status = True
                not_found = False
                role = row[2]
            else: 
                login_status = False
                not_found = False
    #Aksi setelah username atau password ditemukan keduanya, salah satu, atau tidak sama sekali
    if not_found == True: 
        print("username tidak terdaftar")
        role = ""
        return role
    else:
        if login_status == False: 
            print("Password salah!")
            role = ""
            return role
        else: 
            print(f"Selamat datang {username}")
            return role"""

def Login_status(): 
    return login_status