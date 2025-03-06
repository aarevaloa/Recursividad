# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 18:34:25 2025

@author: USUARIO
"""

# secuencia de Fibonacci

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Salida: 55

# Algoritmo de selección recursiva

def select_sort_rec(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        min_index = b.index(min(b))
        aux = b[min_index]
        b[min_index] = b[0]
        b[0] = aux
        return [aux] + select_sort_rec(b[1:])
    
# Variante recursiva del algoritmo de ordenación por selección
    
def select_sort_rec_alt(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)
        return [m] + select_sort_rec_alt(b)