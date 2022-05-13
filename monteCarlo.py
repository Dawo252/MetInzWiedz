import matplotlib.pyplot as plt
import numpy as np
from random import random

def MonteCarlo(poczatekx, koniecx, poczateky, koniecy, funkcja, przejscia):
    losowe = []
    wyzej = 0
    nizej = 0
    for i in range(przejscia):
        losowe.append(((random() * (koniecx - poczatekx)), (random() * (koniecy - poczateky))))
    for each in losowe:
        if(funkcja(each[0])<each[1]):
            wyzej = wyzej +1
        elif(funkcja(each[0])>each[1]):
            nizej = nizej +1
    return nizej/wyzej, losowe

def funkcja(x):
    return x**3

wartosc, losowe = MonteCarlo(0, 1, 0 ,1, funkcja, 5000)
print(wartosc)
listax = []
listay = []
for each in losowe:
    listax.append(each[0])
    listay.append(each[1])

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.xlabel('oś x')
plt.ylabel('oś y')

plt.title('wykres y=x^2')

plt.scatter(listax, listay)
x=np.arange(0, 1, 1/10000)
listay =[]
y = funkcja(x)
plt.plot(x,y, 'red')
plt.show()

def prostokaty(funkcja, ilosc, poczatekx, koniecx):
    szer_prostokata = (koniecx-poczatekx)/ilosc
    prostokaty_lista = []
    powierzchnia = 0
    for i in range(ilosc):
        prostokaty_lista.append((funkcja(poczatekx+szer_prostokata*i), szer_prostokata))
    for each in prostokaty_lista:
        powierzchnia = powierzchnia + each[0] * each[1]
    return powierzchnia

calka = prostokaty(funkcja, 1000, 0, 1)
print(calka)

#### prostokąty działają na pewno, monte carlo chyba nie, ale nie bardzo wiem dlaczego (prawie na pewno błąd w moim myśleniu o tym)