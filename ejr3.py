import csv

filas = []
with open('naves.csv', 'r') as f:
    reader = csv.reader(f)
    
    for i in reader:
        if i[0] == 'Nombre':
            keys = i
            del i
        else:
            filas.append(i)

def info(nave):
    nombre = keys.index('Nombre')
    for i in filas:
        if i[nombre] == nave:
            print(i)
info("Halcon Milenario")
info("Estrella de la Muerte")

def mas_pasajeros():
    nombre = keys.index('Nombre')
    capacidad = keys.index('Capacidad')
    solucion = []
    lista = []
    for i in filas:
        lista.append(int(i[capacidad]))
    for i in range(len(lista)-5):
        lista.remove(min(lista))
    for i in filas:
        for j in range(len(lista)):
            if int(i[capacidad])==lista[j]:
                solucion.append(i[nombre])
    print(solucion)
mas_pasajeros()

def mas_tripulacion():
    nombre = keys.index('Nombre')
    tripulacion = keys.index('Tripulacion')
    lista = []
    for i in filas:
        lista.append(int(i[tripulacion]))
    maxim = max(lista)
    for i in filas:
        if int(i[tripulacion])==maxim:
            solucion = i[nombre]
    print(solucion)
mas_tripulacion()

def at():
    nombre = keys.index('Nombre')
    for i in filas:
        nave = i[0]
        if nave[:2] == 'AT':
            print(nave)
at()

def pasajeros():
    nombre = keys.index('Nombre')
    capacidad = keys.index('Capacidad')
    solucion = []
    lista = []
    for i in filas:
        if int(i[capacidad]) >= 6:
            lista.append(int(i[capacidad]))
    for i in filas:
        for j in range(len(lista)):
            if int(i[capacidad])==lista[j]:
                solucion.append(i[nombre])
    print(solucion)
pasajeros()