import numpy as np


def projekcja(u,v):
    licznik = np.dot(v.T, u)
    mianownik = np.dot(u.T, u)
    return (licznik/mianownik) * u

def normalizacja_u(u):
    return pow(np.dot(u.T, u), 1/2)

print(normalizacja_u(np.array([[1, 0], [2,1]])))
print(np.array([[1, 0], [2,1]]).shape[0])

a=np.array([[2,0],[0,1],[1,1]])


def rozklad(a):
    macierzV = [[x[i] for x in a] for i in range(len(a[1]))]
    macierzU = []
    macierzQ = []
    for vect in macierzV:
        vect = np.array(vect)
        projekcje = 0
        for each in macierzU:
            each = np.array(each)
            projekcje = projekcja(each, vect)
        u = vect - projekcje
        macierzU.append(u)
        if(normalizacja_u(u) == 0):
            e = u
        else:
            e = (1/normalizacja_u(u))*u
        macierzQ.append(e)
    return np.array(macierzQ)

print(rozklad(np.array([[1, 0], [2,1]])))