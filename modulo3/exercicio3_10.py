import numpy as np
print('Matriz:') 
matriz = \
    np.array([[input('0,0: '), input('0,1: '), input('0,2: ')], 
              [input('1,0: '), input('1,1: '), input('1,2: ')]]) 
print(matriz*5)