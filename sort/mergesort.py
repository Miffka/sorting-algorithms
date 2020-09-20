#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

''' BIG O
melhor caso - O(n log(n))
caso comum - O(n log(n))
pior caso - O(n log(n))
'''

def merge(A, p, q, r):
    L = A[p:q]
    R = A[q:r] 
    L.append(10**10)
    R.append(10**10)
    
    i = 0
    j = 0
    
    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
 
def sort(A, p=None, r=None):
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    if p < r - 1:
        q = (p + r)//2
        sort(A, p, q) 
        sort(A, q, r)
        merge(A, p, q, r)
    return A
