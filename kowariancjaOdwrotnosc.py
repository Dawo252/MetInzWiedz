import numpy as np

def kowariancja(macierz):
    return np.dot(macierz.T,macierz)

def odwrotnosc(macierz):
    return np.linalg.inv(macierz)

def lewa_odwrotnosc(macierz):
    return np.dot(odwrotnosc(kowariancja(macierz)),macierz.T)

def regresja(macierz):
    macierzX = []
    macierzY = []
    for x in macierz:
        macierzX.append([1, x[0]])
    for y in macierz:
        macierzY.append(y[1])
    macierzXNP = np.array(macierzX)
    macierzYNP = np.array(macierzY)
    return np.dot(lewa_odwrotnosc(macierzXNP), macierzYNP)

x_y=np.array([[3,3],[6,2],[5,2],[6,5]])
print(regresja(x_y))