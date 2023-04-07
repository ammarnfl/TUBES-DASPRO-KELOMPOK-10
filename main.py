#Program utama ada disini
from login import *
from helps import *
import os


role = ""
while True: 
    masukkan = input(">>> ")
    if masukkan == "login" and role == "": 
        while role =="": 
            role = Login()
    if masukkan == "logout": 
        role = ""
    if role == "jin_pembangun" and masukkan == "bagun": 
        #
    if role == "jin_pengumpul" and masukkan == "bruh":
        #
    if role == "roro_jonggrang":
        #
    if masukkan == "help": 
        #
    if masukkan == "exit": 
        exit()

    