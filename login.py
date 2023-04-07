import csv 
from OurList import *

login_status = False
role_status = False
not_found = False
f = open('user.csv', 'r+')
reader = csv.reader(f, delimiter=";")

username = input("Username: ")
password = input("Password: ")

#check username ada atau tidak
username_check = []
for row in reader: 
    username_check = appends(username_check,row[0])
    if row[0] == username and row[1] == password: 
            login_status = True


for i in range(Length(username_check)): 
    if username == username_check[i] : 
        not_found = False
        break
    else: 
        not_found = True

if not_found == True: 
    print("username tidak terdaftar")
else:
    if login_status == False: 
        print("Password salah")
    else: 
        print("Anda benar")

