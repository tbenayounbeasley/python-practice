#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:57:29 2026

@author: taliabenayoun-beasley
"""

# Q2 : egal(L1, L2)

def egal_listes(L1,L2):
    if len(L1) != len(L2):
        return False
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            return False
    return True


# Q3b : revStr sans slicing

def revStr(s):
    t = ""
    for i in range(len(s) - 1, -1, -1):
        t += s[i]
    return t


# Q4 : revInt(n) = R(n)

def revInt(n):
    if n < 0:
        raise ValueError("n doit être dans N")
    return int(revStr(str(n)))


# Q5a : estLC(C)

def estLC(C):
    for x in C:
        if not (0 <= x <= 9):
            return False
    return True

# Complexite de O(n) 


# Q6a : dictC(C)

def dictC(C):
    if not estLC(C):
        raise ValueError("C n'est pas une liste de chiffres")
    d = {}
    for x in C:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

#Complexite de O(n)


# Q7 : triCPT(C) -> T (tri des chiffres non nuls)

def triCPT(C):
    counts = [0] * 10
    for x in C:
        counts[x] += 1
    T = []
    for digit in range(1, 10):
        if counts[digit]:
            T.extend([digit] * counts[digit])
    return T


# Q8 : int_to_LC(n) sans str

def int_to_LC(n):
    if n < 0:
        raise ValueError("n doit être dans N")
    if n == 0:
        return [0]
    C = []
    while n > 0:
        n, r = divmod(n, 10)
        C.append(r)
    C.reverse()
    return C


# Q9a : estTriee(L)

def estTriee(L):
    for i in range(1, len(L)):
        if L[i-1] > L[i]:
            return False
    return True


# Q9b : LC_to_int(C)

def LC_to_int(C):
    if not estTriee(C):
        raise ValueError("C n'est pas triée")
    if C == []:
        return 0
    n = 0
    for x in C:
        n = 10 * n + x
    return n


# Q10 : triInt(n) = S(n) sans str

def triInt(n):
    C = int_to_LC(n)
    T = triCPT(C)
    return LC_to_int(T)



# Q11 : RATS(n) = S(n + R(n))

def RATS(n):
    if n < 0:
        raise ValueError("n doit être >= 0")
    return triInt(n + revInt(n))


# Q15 : periodeV1 

def periodeV1(k0):
    if k0 < 0:
        raise ValueError("k0 doit être dans N")
    vus = {}
    u = k0
    for n in range(1001):
        if n == 1000:
            return 0
        if u in vus:
            return n - vus[u]
        vus[u] = n
        u = RATS(u)
    return 0


# Q16 : toutesPeriodes

def toutesPeriodes(k0_max):
    if k0_max < 0:
        raise ValueError("k0_max doit être >= 0")
    return [periodeV1(k) for k in range(k0_max + 1)]


# Q17 : minPeriode(p)

A = {0, 1, 2, 3, 8, 14, 18}

def minPeriode(p):
    if p not in A:
        raise ValueError("p n'appartient pas à A")
    k = 0
    while True:
        if periodeV1(k) == p:
            return k
        k += 1


# Q19 : periodeV2 en supposant vraie la conjecture 14

def _est_am_bm(u):
    s = str(u)
    if s.startswith("12") and s.endswith("4444"):
        mid = s[2:-4]
        if len(mid) >= 2 and all(ch == "3" for ch in mid):
            return True
    if s.startswith("55") and s.endswith("7777"):
        mid = s[2:-4]
        if len(mid) >= 2 and all(ch == "6" for ch in mid):
            return True
    return False

def periodeV2(k0):
    if k0 < 0:
        raise ValueError("k0 doit être dans N")
    vus = {}
    u = k0
    n = 0
    while True:
        if _est_am_bm(u):
            return 0
        if u in vus:
            return n - vus[u]
        vus[u] = n
        u = RATS(u)
        n += 1