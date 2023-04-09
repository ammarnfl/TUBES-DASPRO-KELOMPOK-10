import csv 
from OurFunction import *


def Login(username, password):
    login_status = False
    not_found = True
    f = open('user.csv', 'r+')
    reader = csv.reader(f, delimiter=";")
    #check username dan password ada atau tidak
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
            return role