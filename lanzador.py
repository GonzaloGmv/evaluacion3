from ejercicio2.ejr2 import *
from ejercicio3.ejr3 import *
from ejercicio5.ejr5 import *
import csv

def main():
    ejr = input("Escriba el numero del ejercicio que desea ejecutar: ")
    if ejr == '2':
        matriz2 = [[4,-1,3],[2,-1,4],[1,2,3]]
        print(determinante_iterativo(matriz2))
        determinante_recursivo(matriz2, 0, 0)
    elif ejr == '3':
        filas = []
        with open('ejercicio3/naves.csv', 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                if i[0] == 'Nombre':
                    keys = i
                    del i
                else:
                    filas.append(i)
        print( 'mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”')
        print(info("Halcon Milenario", keys, filas))
        print(info("Estrella de la Muerte", keys, filas))
        print( '\ndeterminar cuáles son las cinco naves con mayor cantidad de pasajeros')
        print(mas_pasajeros(keys, filas))
        print( '\nindicar cuál es la nave que requiere mayor cantidad de tripulación')
        print(mas_tripulacion(keys, filas))
        print( '\nmostrar todas las naves que comienzan con AT')
        at(filas)
        print( '\nlistar todas las naves que pueden llevar seis o más pasajeros')
        print(pasajeros(keys, filas))
        print( '\n mostrar toda la información de la nave más pequeña y la más grande')
        ordenar(keys, filas)
    elif ejr == '5':
        print("\nApartado 1 \n")
        ejr5_1(input('Escriba el mensaje que desea codificar (se mostraran solo los 8 primeros caracteres): '))
        print("\nApartado 2 \n")
        mensaje = input("Escriba el mensaje que desea codificar y posteriormente descodificar, siempre que el codigo ASCII de sus caracteres este entre el 32 y el 125: ")
        ejr5_2_desencriptar(ejr5_2_encriptar(mensaje))