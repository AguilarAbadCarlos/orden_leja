# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:19:51 2023

@author: Carlos Aguilar
"""

import numpy as np

def orden_leja(x):
    x = np.array(x)                 
    n=len(x)
    Idx = np.zeros(n,dtype='int')   # Vector de enteros para almacenar los indices ordenados
    
    M = np.zeros([n,n])             # Matriz de diferencias entre todas las
    for i in range(0,n-1):          # parejas posibles de nodos. Se guarda
        for j in range(i+1,n):      # para no repetir los calculos
            M[i,j]=x[i]-x[j] 
    M = np.abs(M+M.T)               # Simetrizacion de M y valor absoluto
    
    m = np.ones(n)                  # Inicializamos vector de productos de diferencias
    k = np.argmax(x)                # Fijamos primer nodo al maximo
    Idx[0] = k
    
    for i in range(1,n):            # Aplicamos el algoritmo al resto de puntos
        m = m * M[Idx[i-1],:]       # Actualizar vector de productos con el nodo anterior
        Idx[i] = np.argmax(m)       # Guardamos posicion que maximiza el producto
    
    return x[Idx]                   # Devolvemos vector ordenado segun Leja

'''
# Tests
x = [0,1./3,2./3,1.]
print('Orden de Leja de',x,':\n\t',orden_leja(x))

x = [0,1./4,2./4,3./4,1.]
print('Orden de Leja de',x,':\n\t',orden_leja(x))
'''