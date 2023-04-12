import csv 
from OurFunction import *
from Z1_ListFunction import *





# cek username ada atau tidak
#username_check = []
# checker = False
# for row in range(lengthI(username_check)):
#    if username == username_check[row] and checker == False:
#        not_found = False
#        checker = True
#    elif checker == False:
#        not_found = True

#if not_found == True:
#    print("Tidak ada jin dengan username tersebut.")
#else:
#    type_checker = 


def ubah_jin():
    f = open('user.csv', 'r+')
    username = input("Masukkkan username Jin: ")
    while True:
        #cek tipe rolenya?
        type_role = "Pengumpul" # cara cek tipe rolenya masih bingung
        if type_role == "Pengumpul":
            YN = input("Jin ini bertipe" "Pengumpul." "Yakin ingin mengubah ke tipe " "Pembangun" "(Y/N)? ")
        else:
            YN = input("Jin ini bertipe" "Pembangun." "Yakin ingin mengubah ke tipe " "Pengumpul" "(Y/N)? ")
    f.close()

# check_username harus update pake parser
def check_username(username): 
    f = open('user.csv', 'r+')
    reader = csv.reader(f, delimiter =';')
    for row in reader: 
        if row[0] == username: 
            f.close()
            return True
    f.close()
    return False
