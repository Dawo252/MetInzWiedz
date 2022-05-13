import collections
import random
import numpy as np

# # slowo = input()
# # print(slowo)
# # liczba = 1000
# # slowo = "slowowow"

# # print(type(liczba))
# # print(type(slowo))

# # print("liczby cos tam cos tam {0}, oraz {1}".format(liczba, slowo))

# slowo1 = ["slsow1", "slsow2", "slsow3", "slsow4", "slsow5"]

# slowo2 = ' '.join(slowo1)
# slowo3 = slowo2.split(' ')

# # print(type(slowo3))

# # jakiesZdanieDoZmiennej = "Metody Inżynierii Wiedzy są najlepsze"

# # print(jakiesZdanieDoZmiennej)
# # print(jakiesZdanieDoZmiennej.lower())

# # jakiesZdanieDoZmiennej2 = jakiesZdanieDoZmiennej.replace('ą','a').replace('ż','z')

# # print(set(jakiesZdanieDoZmiennej2), len(set(jakiesZdanieDoZmiennej2)), len(jakiesZdanieDoZmiennej2))

# # string1 = "dasdad"
# # napis = "s"
# # tupka = ((string1, napis))
# # print(tupka, type(tupka))

# # lista1 = ['c', 'b', 'a']
# # lista2 = [2, 1, 3]
# # lista4 = [9, 9, 7]
# # print(lista1 + lista2, type(lista1+lista2))

# # lista3 = lista1 + lista2
# # print(lista3.index('c'))

# # lista2.extend(lista4)
# # lista2.append(9)
# # print(lista2)

# # slownik = {'pierwszyElement': 2}
# # print(slownik)

# print(bool(""))
# print(bool(" "))
# print(bool(0))
# print(bool(1))
# print(bool('0'))
# print(bool('1'))
# print(bool([]))
# print(bool(['']))

# for i in range(21):
#     print(i)

# print(slowo2)


# def split2(slowo2, luka):
#     lista = []
#     slowo = ""
#     for x in slowo2:
#         if x != luka:
#             slowo+=x
#         else:
#             lista.append(slowo)
#             slowo = ""
#     return lista

# print(split2(slowo2, " "))

# haslo = "Duzemaleee!"


# rozmiar = False
# duze = False
# specjalne = False
# male = False
# if(len(haslo) >= 10):
#     rozmiar = True
#     for litera in set(list(haslo)):
#         if(litera.isupper() and litera is not "!"):
#             duze = True
#         if(litera.islower() and litera is not "!"):
#             male = True
#         if(litera == "!"):
#             specjalne = True
# print((rozmiar and duze and specjalne and male), "mocne haslo")

# lista = [1, 9, 99, 98, 3]

# for i in lista:
#     if i is not 99:
#         print(i)

# i = 0
# while(i < len(lista)-1):
#     if(lista[i]==99):
#         print(i)
#         break
#     i+=1

# with open("C:/Users/local/Documents/costam.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         #print(line.replace("\n",""))
#         print(line, end='')

# with open("C:/Users/local/Documents/costam.txt", 'r', encoding='utf-8') as f:
#     print("\n")
#     print("".join(f.readlines()))

# listaJezykow = ["C", "C++", "Java", "Python", "Pascal", "Haskel", "Basic", "VisualBasic", "Go"]

# with open("C:/Users/local/Documents/costam.txt", 'w', encoding='utf-8') as f:
#     for i in listaJezykow:
#         print(i, file=f)

listaF = []

with open("australian.dat") as ausF:
    for i in ausF:
        listaF.append(list(map(lambda s: float(s), i.split())))


# def odlEuklidesowa(lista):
#     suma = 0
#     slownik = collections.defaultdict(list)
#     for x in listaF:
#         for y in range(len(lista)):
#             suma += pow(lista[y] - x[y], 2)
#         wynik = pow(suma, 1 / 2)
#         slownik[x[len(lista) - 1]].append(wynik)
#         wynik = 0
#     return slownik


# slownik2 = odlEuklidesowa(listaF[1])
# print(slownik2[1])


def odlEuklidesowa(lista, lista2):
    suma = 0
    for y in range(len(lista)):
        suma += pow(lista[y] - lista2[y], 2)
    return pow(suma, 1 / 2)


# odlEuklidesowa2(listaF[0], listaF[500])

x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def mierzymy(x, listaF):
    listaT = []
    slownik = collections.defaultdict(list)
    for z in listaF:
        tupka = (z[len(z) - 1], odlEuklidesowa(x, z))
        listaT.append(tupka)
    return listaT


def mierzymy2(x, listaF):
    slownik = collections.defaultdict(list)
    for z in listaF:
        slownik[z[len(z) - 1]].append(odlEuklidesowa(x, z))
    return slownik


def grupujemy(listaT, n):
    suma = 0
    wynik = 0
    listaOdl = []
    slownik = collections.defaultdict(list)
    listaT.sort()
    for t in listaT:
        slownik[t[0]].append(t[1])
    for i in range(len(slownik.keys())):
        for j in range(n):
            wynik = wynik + slownik[i][j]
        listaOdl.append(wynik)
        wynik = 0
    return slownik




listaT = mierzymy2(x, listaF)
print(listaT[0.0])

# slownikT = grupujemy(listaT, 5)
# print(slownikT)
print(listaF)

def metrEuklidesowa2(lista, lista2):
    v1 = np.array(lista)
    v2 = np.array(lista2)
    a = v1 - v2
    return pow(np.dot(a, a), 1/2)

listaBezDecyzyjnej = []
vector1 = []
for vector in listaF:
    listaBezDecyzyjnej.append(vector)

for each in range(len(listaF)):
    listaBezDecyzyjnej[each].pop()

print(listaBezDecyzyjnej)

for each2 in range(len(listaBezDecyzyjnej)):
    listaBezDecyzyjnej[each2].append(random.randint(float(0),float(1)))
print(listaBezDecyzyjnej)
def srodkiCiezkosci(listaBezDecyzyjnej):
    sumaZer = []
    sumaJedynek = []
    for each in listaBezDecyzyjnej:
        slownik = mierzymy2(each, listaBezDecyzyjnej)
        sumaZer.append(sum(slownik[0.0]))
        sumaJedynek.append(sum(slownik[1.0]))
    return [sumaZer.index(min(sumaZer)), sumaJedynek.index(min(sumaJedynek))]

def dodajNowy(listaBezDecyzyjnej, vector):
    srdkiCiezkosci = srodkiCiezkosci(listaBezDecyzyjnej)
    if(metrEuklidesowa2(vector, listaBezDecyzyjnej[srdkiCiezkosci[0]])< metrEuklidesowa2(vector, listaBezDecyzyjnej[srdkiCiezkosci[1]])):
        vector.append[0]
    elif(metrEuklidesowa2(vector, listaBezDecyzyjnej[srdkiCiezkosci[0]])> metrEuklidesowa2(vector, listaBezDecyzyjnej[srdkiCiezkosci[1]])):
        vector.append[1]
    else:
        vector.append(None)
    return vector

def przypiszKlase(listaBezDecyzyjnej):
    counter1 = 0
    counter0 = 0
    counterAll = 20
    while(counterAll > 0):
        counter0 = 0
        counter1 = 0
        srdkiCiezkosci = srodkiCiezkosci(listaBezDecyzyjnej)
        for each in listaBezDecyzyjnej:
            if(metrEuklidesowa2(each, listaBezDecyzyjnej[srdkiCiezkosci[0]]) == metrEuklidesowa2(each, listaBezDecyzyjnej[srdkiCiezkosci[1]])):
                each[14] = each[14]
            elif((metrEuklidesowa2(each, listaBezDecyzyjnej[srdkiCiezkosci[0]]) > metrEuklidesowa2(each, listaBezDecyzyjnej[srdkiCiezkosci[1]])) and each[14] == 0):
                each[14] = 1
                counter1 = counter1 + 1
            elif((metrEuklidesowa2(each, listaBezDecyzyjnej[srdkiCiezkosci[0]]) < metrEuklidesowa2(each, listaBezDecyzyjnej[srdkiCiezkosci[1]]))and each[14] == 1):
                each[14] = 0
                counter0 = counter0 + 1
        counterAll = counter0 + counter1
    return(listaBezDecyzyjnej)


# lista = srodkiCiezkosci(listaBezDecyzyjnej)
# print(lista[0])
lista = przypiszKlase(listaBezDecyzyjnej)
suma0 = 0
suma1 = 0
for each in lista:
    if(each[14] == 0):
        suma0 = suma0 + 1
    else:
        suma1 = suma1 + 1
print(suma0, suma1)
