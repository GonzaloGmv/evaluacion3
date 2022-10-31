import hashlib

def ejr5_1(mensaje):
    for i in range(len(mensaje)):
        salida = hashlib.sha256(mensaje[i].encode('utf-8')).hexdigest()
        print(salida[:8])
    
def ejr5_2_encriptar(mensaje):
    caracter = []
    encrip = []
    for i in mensaje:
        caracter.append(i)
    for i in caracter:
        if ord(i) >= 32 and ord(i) <= 125:
            encrip.append(hashlib.sha256(i.encode('utf-8')).hexdigest())
    return encrip

def ejr5_2_desencriptar(encriptado):
    for i in encriptado:
        for j in range(32, 126):
            if hashlib.sha256(chr(j).encode('utf-8')).hexdigest() == i:
                print(chr(j))
