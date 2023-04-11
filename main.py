import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="Usage python3 main.py <nama_folder>")
args = parser.parse_args()

if(os.path.isdir(args.nama_folder) == True): 
    print("Selamat datang di program Manajerial candi")
    print("silahkan masukkan username anda")
else: 
    print("Folder tidak ada")