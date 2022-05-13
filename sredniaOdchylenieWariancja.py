with open("australian.dat","r") as file:
    macierz = [list(map(lambda a: float(a),line.split())) for line in file]

def srednia(lista):
    suma = 0
    for wartosc in lista:
        suma = suma + wartosc
    srednia_ar = suma/len(lista)
    return srednia_ar

def wariancja(lista):
    suma = 0
    srednia_ar = srednia(lista)
    for wartosc in lista:
        suma = suma + (wartosc - srednia_ar)*(wartosc - srednia_ar)
    wariancja = suma/len(lista)
    return wariancja

def odchylenie_standardowe(lista):
    odchylenie_standardowe = pow(wariancja(lista), 1/2)
    return odchylenie_standardowe

macierz1 = [x[:14] for x in macierz]
print(srednia(macierz1[0]))
print(wariancja(macierz1[0]))
print(odchylenie_standardowe(macierz1[0]))
