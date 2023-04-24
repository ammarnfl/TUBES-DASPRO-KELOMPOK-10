data_list = []

# melakukan loop untuk membuat entri untuk setiap data
for i in range(1, 101):
    # menggabungkan data menjadi satu string
    data = f"waduh{i:02d};12345;jin_pembangun"
    # menambahkan data ke dalam list
    data_list.append(data)

# menampilkan list data
for data in data_list:
    print(data)