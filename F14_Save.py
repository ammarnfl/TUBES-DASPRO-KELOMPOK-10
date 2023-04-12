import os 
from main import Memory as M

def save(path):
    if not os.path.exists(path):
        os.makedirs(path)
        f = open(os.path.join(path, 'users.txt'), 'w')
        f.close()
    else: 
        f =  open(os.path.join(path, 'users.txt'), 'w')
        f.close()

print(M()[0])
"""
def write_data(): 
    #define here
    break"""

