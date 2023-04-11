from Z2_CSV_Function import *
from os import *
f = open('user.csv', 'r+')
a = f.readlines()
f.close 

g = [None for i in range(Neff)]
g = matriks_csv(a)
print(g)

username = input()
i = 0
while g[i]!= Mark: 
    print(g[i])
    if g[i][0] == username: 
        print("ketemu")
        break
    i += 1
if Marking(g[i]) == True: 
    print("ga ketemu")

print(path.exist("data"))