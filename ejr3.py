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
    indice = keys.index('Nombre')
    for i in filas:
        if i[indice] == nave:
            print(i)
info("Halcon Milenario")
info("Estrella de la Muerte")