#Program utama ada disini
from login import *
from helps import *
import os


role = ""
while True: 
    masukkan = input(">>> ")
    if masukkan == "login" and role == "": 
        role = Login()
    if masukkan == "logout": 
        role = ""
    if role == "jin_pembangun" and masukkan == "bagun": 
        print()
    if role == "jin_pengumpul" and masukkan == "bruh":
        print()
    if role == "roro_jonggrang":
        print()
    if masukkan == "help": 
        helps()
    if masukkan == "exit": 
        exit()
    print(role)
    