import numpy as np
print('Matriz 1') 
matriz_1 = np.array([[input('0,0: '), input('0,1: ')], 
    [input('1,0: '), input('1,1: ')]]) 
print('Matriz 2') 
matriz_2 = np.array([[input('0,0: '), input('0,1: ')], 
    [input('1,0: '), input('1,1: ')]])
print(matriz_1 + matriz_2)