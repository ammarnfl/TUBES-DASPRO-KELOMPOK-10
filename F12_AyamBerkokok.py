from Z1_ListFunction import * 

def AyamBerkokok (array_of_candi: list) -> str:
    print("Kukuruyuk.. Kukuruyuk..")
    count_candi = Len(array_of_candi)
    print(f"Jumlah candi: {count_candi}")

    if count_candi >= 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    exit