def info(nave, keys, filas):
    nombre = keys.index('Nombre')
    for i in filas:
        if i[nombre] == nave:
            print(i)

def mas_pasajeros(keys, filas):
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

def mas_tripulacion(keys, filas):
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

def at(filas):
    for i in filas:
        nave = i[0]
        if nave[:2] == 'AT':
            print(nave)

def pasajeros(keys, filas):
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

def ordenar(keys, filas):
    largo = keys.index('Largo')
    lista = []
    for i in filas:
        lista.append(float(i[largo]))
    lista.sort()
    for i in filas:
        if float(i[largo])==lista[0]:
            print("La nave mas pequeña es", i)
        elif float(i[largo])==lista[-1]:
            print("La nave mas grande es", i)