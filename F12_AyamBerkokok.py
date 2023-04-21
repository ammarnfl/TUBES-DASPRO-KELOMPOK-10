from Z1_ListFunction import * 
from typing import Any

def AyamBerkokok (array_of_candi: list) -> Any:
    print("\nKukuruyuk.. Kukuruyuk..")
    count_candi = 0
    for i in range(0, Len(array_of_candi)): 
        if Len(array_of_candi[i]) != 1: 
            count_candi += 1
    count_candi -= 1
    print(f"Jumlah candi: {count_candi}")

    if count_candi >= 100:
        print("\nYah, Bandung Bondowoso memenangkan permainan!")
    
    else:
        print("\nSelamat, Roro Jonggrang memenangkan permainan!")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.\n")
    
    return exit()