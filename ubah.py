import csv 
from OurFunction import *

# type = file jenis jin
not_found = False
f = open('user.csv', 'r+')
reader = csv.reader(f, delimiter=";")

username = input("Masukkkan username Jin: ")

# cek username ada atau tidak
username_check = []
checker = False
for row in range(lengthI(username_check)):
    if username == username_check[row] and checker == False:
        not_found = False
        checker = True
    elif checker == False:
        not_found = True

if not_found == True:
    print("Tidak ada jin dengan username tersebut.")
else:
    type_checker = 