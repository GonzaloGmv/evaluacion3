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


print(keys)
for i in range(len(filas)):
    print(filas[i])